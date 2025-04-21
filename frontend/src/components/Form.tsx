import { Check, Database, Globe, LinkIcon } from "lucide-react";
import Button from "./Button";
import { useState, useRef, useEffect, useCallback } from "react";

const dataTypes = [
  { value: "email", label: "Email" },
  { value: "phone", label: "Phone" },
  { value: "birthdate", label: "Birthdate" },
  { value: "passport", label: "Passport (series and number)" },
  { value: "zip", label: "Postal Code" },
  { value: "country", label: "Country (Russia, USA, UK)" },
  { value: "address", label: "Address" },
  { value: "snils", label: "SNILS" },
  { value: "inn", label: "INN" },
  { value: "cardNumber", label: "Bank Card Number" },
  { value: "iban", label: "IBAN" },
  { value: "paymentAmount", label: "Payment Amount" },
  { value: "vin", label: "VIN" },
  { value: "orderDate", label: "Order Date" },
  { value: "time", label: "Time" },
  { value: "url", label: "URL" },
  { value: "carNumber", label: "Car Number" },
  { value: "password", label: "Password" },
  { value: "macAddress", label: "MAC Address" },
  { value: "coordinates", label: "Coordinates" },
];

const Form = () => {
  const [selectedItem, setSelectedItem] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);

  const filteredItems = useCallback(() => {
    const term = searchTerm.toLowerCase();
    return dataTypes.filter((item) => item.label.toLowerCase().includes(term));
  }, [searchTerm]);

  const handleItemClick = (item) => {
    setSelectedItem(item.label);
    setIsDropdownOpen(false);
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [dropdownRef]);

  return (
    <form className="border-foreground/20 flex min-w-sm flex-col gap-4 space-y-4 rounded-xl border p-8 shadow">
      <div className="flex items-center space-x-2">
        <Globe className="text-foreground size-5" />
        <h1 className="text-lg font-bold">URL Data Validator</h1>
      </div>

      <div className="space-y-2">
        <label htmlFor="url" className="flex items-center gap-2 font-medium">
          <LinkIcon className="text-foreground size-4" />
          URL
        </label>
        <div className="relative">
          <input
            type="text"
            id="url"
            className="bg-background placeholder:text-foreground/30 hover:border-foreground/40 focus:border-foreground/50 border-foreground/30 w-full rounded-lg border px-10 py-2 text-sm duration-200 ease-in-out focus:outline-none"
            placeholder="https://example.com/data"
          />
          <div className="text-primary absolute top-1/2 left-3 -translate-y-1/2">
            <Globe className="size-5" />
          </div>
        </div>
      </div>

      <div className="space-y-2">
        <label
          htmlFor="data-type"
          className="flex items-center gap-2 font-medium"
        >
          <Database className="text-primary h-5 w-5" />
          Data Type
        </label>
        <div className="relative" ref={dropdownRef}>
          <input
            type="text"
            id="data-type"
            className="bg-background placeholder:text-foreground/30 hover:border-foreground/40 focus:border-foreground/50 border-foreground/30 w-full rounded-lg border px-3 py-2 text-sm duration-200 ease-in-out focus:outline-none"
            placeholder="Search data type..."
            value={selectedItem || searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setSelectedItem("");
            }}
            onFocus={() => setIsDropdownOpen(true)}
            onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          />
          {isDropdownOpen && (
            <div className="bg-background border-foreground/30 absolute left-0 z-10 mt-1 flex max-h-40 w-full flex-col gap-0.5 overflow-y-auto rounded-md border p-1 shadow-lg">
              {filteredItems().length > 0 ? (
                filteredItems().map((item) => (
                  <button
                    key={item.label}
                    className="rounded px-4 py-1 text-start text-xs hover:bg-[#27272a]"
                    onClick={() => handleItemClick(item)}
                  >
                    {item.label}
                  </button>
                ))
              ) : (
                <div className="text-foreground/50 px-4 py-2">
                  No items found
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      <div>
        <Button className="w-full">
          <Check />
          Validate Data
        </Button>
      </div>
    </form>
  );
};

export default Form;
