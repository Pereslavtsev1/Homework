import { ReactNode } from "react";

type ButtonProps = {
  children: ReactNode;
  className?: string;
  onClick?: () => void;
};

const Button = ({ children, className }: ButtonProps) => {
  return (
    <button
      className={`${className} bg-foreground text-background hover:bg-foreground/95 flex cursor-pointer items-center gap-2 rounded-xl px-5 py-2 text-sm font-medium`}
    >
      {children}
    </button>
  );
};

export default Button;
