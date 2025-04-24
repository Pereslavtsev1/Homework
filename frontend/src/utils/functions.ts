import { DataType, ValidationResult } from "../types";
export const validate = (data: string, type: string): ValidationResult => {
  if (!data) {
    return { isValid: false, message: "Input data is empty." };
  }
  console.log(type);
  switch (type) {
    case DataType.EMIAL:
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (emailRegex.test(data)) {
        return { isValid: true, message: "Email address is valid." };
      } else {
        return { isValid: false, message: "Invalid email address format." };
      }

    case DataType.PHONE:
      const allowedCharsRegex = /^[0-9\s()+-]+$/;

      if (!allowedCharsRegex.test(data)) {
        return {
          isValid: false,
          message:
            "Phone number contains invalid characters. Only digits, spaces, (), +, - are allowed.",
        };
      }

      const digitsOnly = data.replace(/\D/g, "");
      const digitCount = digitsOnly.length;

      if (digitCount === 11) {
        if (digitsOnly.startsWith("7") || digitsOnly.startsWith("8")) {
          return {
            isValid: true,
            message: "Phone number is valid.",
          };
        } else {
          return {
            isValid: false,
            message: `11-digit phone number must start with 7 or 8 (found ${digitsOnly.charAt(0)}).`,
          };
        }
      } else {
        return {
          isValid: false,
          message: `Phone number has an incorrect number of digits (${digitCount}). Expected exactly 11.`,
        };
      }

    case DataType.BANK_CARD_NUMBER:
      const cardNumberRegex = /^\d{13,19}$/;

      if (!cardNumberRegex.test(data)) {
        return {
          isValid: false,
          message: "Invalid bank card number format (must be 13-19 digits).",
        };
      }

      let sum = 0;
      let parity = data.length % 2;

      for (let i = 0; i < data.length; i++) {
        let digit = parseInt(data[i]);

        if (i % 2 === parity) {
          digit *= 2;
          if (digit > 9) {
            digit -= 9;
          }
        }
        sum += digit;
      }

      if (sum % 10 === 0) {
        return {
          isValid: true,
          message: "Bank card number is valid (Luhn check passed).",
        };
      } else {
        return {
          isValid: false,
          message: "Bank card number failed Luhn algorithm check.",
        };
      }

    case DataType.COORDINATES:
      const coordsRegex =
        /^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?(\s*,\s*-?\d+(\.\d+)?)?\s*$/;

      if (!coordsRegex.test(data)) {
        return {
          isValid: false,
          message:
            "Invalid coordinates format (expected 'lat, lon' or 'lat, lon, alt').",
        };
      }

      const parts = data.split(",").map((part) => parseFloat(part.trim()));
      const latitude = parts[0];
      const longitude = parts[1];

      if (isNaN(latitude) || isNaN(longitude)) {
        return {
          isValid: false,
          message: "Failed to parse latitude or longitude.",
        };
      }

      if (
        latitude < -90 ||
        latitude > 90 ||
        longitude < -180 ||
        longitude > 180
      ) {
        return {
          isValid: false,
          message:
            "Coordinates are out of valid range (latitude -90 to 90, longitude -180 to 180).",
        };
      }

      return { isValid: true, message: "Coordinates are valid." };

    default:
      return {
        isValid: false,
        message: `Unknown data type for validation: "${type}".`,
      };
  }
};
