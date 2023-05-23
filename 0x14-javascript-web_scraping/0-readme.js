#!/usr/bin/node

const fs = require('fs');

//reading file using fs.readfile

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (err, content) => {
    if (err) {
      console.error(`Error occurred while reading the file: ${err}`);
    } else {
      console.log(content);
    }
  });
}

//checking for the file path
if (process.argv.length < 3) {
  console.error('Please provide the file path as an argument.');
  process.exit(1);
}

const filePath = process.argv[2];
readFile(filePath);
