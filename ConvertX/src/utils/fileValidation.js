export function validateSize(file, maxSize = 50 * 1024 * 1024) {
  if (!file) {
    return {
      valid: false,
      message: "Please select a file.",
    };
  }

  if (file.size > maxSize) {
    return {
      valid: false,
      message: "Maximum file size is 50MB.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}

export function validateType(file, allowedTypes) {
  if (!allowedTypes.includes(file.type)) {
    return {
      valid: false,
      message: "Unsupported file type.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}

export default {
  validateSize,
  validateType,
};