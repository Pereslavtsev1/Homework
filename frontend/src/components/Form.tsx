import { Check, Database, Globe, LinkIcon } from "lucide-react";

import Button from "./Button";

import { useState, useRef, useEffect, useCallback } from "react";

import { DataType } from "../types";

import { toast } from "sonner";

import { Toaster } from "sonner";

import FormHeader from "./form/FormHeader";

import { validate } from "../utils/functions";

const Form = () => {
  const [selectedItem, setSelectedItem] = useState<string>("");
  const [searchTerm, setSearchTerm] = useState("");
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [url, setUrl] = useState("");
  const dropdownRef = useRef<HTMLDivElement>(null);
  const allDataTypes = Object.values(DataType);

  const filteredItems = useCallback(() => {
    const term = searchTerm.toLowerCase();

    return allDataTypes.filter((label) => label.toLowerCase().includes(term));
  }, [searchTerm, allDataTypes]);

  const handleItemClick = (label: string) => {
    setSelectedItem(label);
    setSearchTerm(label);
    setIsDropdownOpen(false);
  };

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setIsDropdownOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [dropdownRef]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!url || !selectedItem) {
      alert("Please enter both URL and select a Data Type.");
      return;
    }

    try {
      const response = await fetch(url, {
        method: "GET",
      });

      if (response.ok) {
        const data = await response.json();

        toast.success("Data fetched successfully!");

        const validationResult = validate(data.content, selectedItem);

        validationResult.isValid
          ? toast.success(validationResult.message)
          : toast.error(validationResult.message);
      } else {
        const errorData = await response
          .json()
          .catch(() => ({ error: "Failed to get error message from server." }));
        const errorMessage =
          errorData.error || `Status code: ${response.status}`;

        toast.error(`Error fetching data: ${errorMessage}`);
      }
    } catch (error) {
      console.error("Fetch error:", error);

      toast.error(
        "An unexpected error occurred. Check the URL or network connection.",
      );
    }
  };

  return (
    <>
      <form
        className="border-foreground/20 bg-background mx-auto w-full max-w-sm space-y-6 rounded-xl border p-8 shadow-lg sm:p-10"
        onSubmit={handleSubmit}
      >
        {/* URL Input Section */}

        <FormHeader />
        <div className="space-y-2">
          <label
            htmlFor="url"
            className="text-foreground flex items-center gap-2 text-sm font-medium"
          >
            <LinkIcon className="text-primary size-4" /> URL
          </label>

          <div className="relative">
            <input
              type="text"
              id="url"
              className="border-foreground/30 bg-background text-foreground placeholder:text-foreground/40 hover:border-foreground/40 focus:border-primary focus:ring-primary w-full rounded-lg border py-2 pr-3 pl-10 text-sm transition-colors duration-200 ease-in-out focus:ring-1 focus:outline-none" // Refined focus styles
              placeholder="https://example.com/data"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
            />

            <div className="text-primary absolute top-1/2 left-3 -translate-y-1/2">
              <Globe className="size-5" />
            </div>
          </div>
        </div>

        {/* Data Type Select Section */}

        <div className="space-y-2">
          <label
            htmlFor="data-type"
            className="text-foreground flex items-center gap-2 text-sm font-medium"
          >
            <Database className="text-primary size-4" /> Data Type
          </label>

          <div className="relative" ref={dropdownRef}>
            <input
              type="text"
              id="data-type"
              className="border-foreground/30 bg-background text-foreground placeholder:text-foreground/40 hover:border-foreground/40 focus:border-primary focus:ring-primary w-full cursor-pointer rounded-lg border py-2 pr-8 pl-3 text-sm transition-colors duration-200 ease-in-out focus:ring-1 focus:outline-none" // Refined focus styles, added cursor
              placeholder="Select or search data type..."
              value={isDropdownOpen ? searchTerm : selectedItem}
              onChange={(e) => {
                setSearchTerm(e.target.value);
                setSelectedItem("");
                setIsDropdownOpen(true);
              }}
              onFocus={() => setIsDropdownOpen(true)}
            />

            {isDropdownOpen && (
              <div className="border-foreground/30 bg-background absolute top-full right-0 left-0 z-10 mt-2 max-h-40 overflow-y-auto rounded-md border p-1 shadow-lg">
                {filteredItems().length > 0 ? (
                  filteredItems().map((itemLabel) => (
                    <button
                      key={itemLabel}
                      className="text-foreground hover:bg-foreground/10 focus:bg-foreground/10 block w-full cursor-pointer rounded px-3 py-2 text-left text-sm font-medium focus:outline-none"
                      onClick={() => handleItemClick(itemLabel)}
                      type="button"
                    >
                      {itemLabel} {/* Display the label */}
                    </button>
                  ))
                ) : (
                  <div className="text-foreground/60 px-3 py-2 text-center text-sm">
                    No items found
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Submit Button */}

        <div>
          <Button type="submit" className="w-full">
            <Check className="mr-2 size-4" />
            Validate Data
          </Button>
        </div>
      </form>

      {/* Sonner Toaster for notifications */}

      <Toaster />
    </>
  );
};

export default Form;
