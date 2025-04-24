import { ReactNode } from "react";

type ButtonProps = {
  children: ReactNode;
  type?: "submit" | "button";
  className?: string;
  onClick?: () => void;
};

const Button = ({
  children,
  type = "button",
  className,
  onClick,
}: ButtonProps) => {
  return (
    <button
      type={type}
      className={`bg-foreground text-background hover:bg-foreground/95 flex cursor-pointer items-center gap-2 rounded-xl px-5 py-2 text-sm font-medium ${className}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
