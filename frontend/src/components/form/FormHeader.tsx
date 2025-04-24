import { Globe } from "lucide-react";

const FormHeader = () => {
  return (
    <div className="flex items-center space-x-3">
      <Globe className="text-primary size-6" />
      <h1 className="text-foreground text-xl font-bold">URL Data Validator</h1>
    </div>
  );
};

export default FormHeader;
