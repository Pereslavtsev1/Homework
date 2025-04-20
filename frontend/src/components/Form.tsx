import { Check, Database, Globe, LinkIcon } from "lucide-react";
import Button from "./Button";

const Form = () => {
  return (
    <form className="border-foreground/20 flex min-w-md flex-col gap-4 space-y-4 rounded-xl border px-10 py-8 shadow">
      <div className="flex items-center space-x-2">
        <Globe className="text-foreground size-5" />
        <h1 className="text-xl font-bold">URL Data Validator</h1>
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
            className="bg-background placeholder:text-foreground/30 hover:border-foreground/40 focus:border-foreground/50 border-foreground/30 w-full rounded-lg border px-10 py-2 duration-200 ease-in-out focus:outline-none"
            placeholder="Enter URL here"
          />
          <div className="text-primary absolute top-1/2 left-3 -translate-y-1/2">
            <Globe className="size-5" />
          </div>
        </div>
      </div>

      <div>
        <label
          htmlFor="data-type"
          className="flex items-center gap-2 text-lg font-medium"
        >
          <Database className="text-primary h-5 w-5" />
          Data Type
        </label>
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
