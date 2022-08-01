#!/usr/bin/node

const tam = process.argv[2];

if (tam === undefined || isNaN(parseInt(tam))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < tam; i++) {
    console.log('X'.repeat(tam));
  }
}
