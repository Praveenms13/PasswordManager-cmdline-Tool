const alphabets = "abcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "@123456789";
const symbols = "!@#$%*&_-+=";

exports.createPassword = (length = 8, isnumbers = true, issymbols = true) => {
  let chars = alphabets;
  isnumbers ? (chars += numbers) : "";
  issymbols ? (chars += symbols) : "";
  return generatePassword(length, chars);
};
generatePassword = (length, chars) => {
  let password = "";
  for (let i = 0; i < length; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return password;
};
