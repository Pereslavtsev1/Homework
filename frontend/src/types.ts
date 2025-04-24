export enum DataType {
  EMIAL = "Email",
  BANK_CARD_NUMBER = "Bank card number",
  PHONE = "Phone",
  COORDINATES = "Coordinates",
}
export type ValidationResult = {
  isValid: boolean;
  message: string;
};
