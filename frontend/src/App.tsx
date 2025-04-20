import Button from "./components/Button";
import { Check } from "lucide-react";

function App() {
  return (
    <>
      <main className="flex h-dvh w-dvw items-center justify-center">
        <Button>
          <Check />
          Validate
        </Button>
      </main>
    </>
  );
}

export default App;
