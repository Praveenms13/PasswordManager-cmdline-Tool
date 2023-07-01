#! /usr/bin/env node
const program = require("commander");
const createPassword = require("./utils/createPassword");
const savePassword = require("./utils/savePassword");
program.version("1.0.0").description("Password Generator");

program
  .option("-l, --length <number>", "length of a password..", "8")
  .option("-s, --save", "Save password to passwords.txt")
  .option("-nn, --no-numbers", "Passwords will be generated without numbers")
  .option("-ns, --no-symbols", "Passwords will be generated without symbols");
program.parse();

const { length, save, numbers, symbols } = program.opts();
const generatedPassword = createPassword.createPassword(
  length,
  numbers,
  symbols
);
if (save) {
    savePassword.savePassword(generatedPassword);
}
console.log("Your Generated Password: ", generatedPassword);
