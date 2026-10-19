import { mkdirSync, copyFileSync } from 'node:fs';
mkdirSync('assets', { recursive: true });
copyFileSync('node_modules/gsap/dist/gsap.min.js', 'assets/gsap.min.js');
console.log('Local GSAP asset ready.');
