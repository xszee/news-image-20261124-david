// news-image-20261124, david account entry.
//
// The front page is drawn by draw.py and shipped next to this file as
// art.png. This program does nothing creative: it checks that art.png is
// a real 1024x1024 PNG inside the 1 MiB gate, then places an exact copy
// at $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
// Node 22, standard library only, no network, same bytes every run.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const sourcePath = new URL("./art.png", import.meta.url);
if (!existsSync(sourcePath)) {
  throw new Error("art.png is missing next to main.ts");
}
const image = readFileSync(sourcePath);

const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (image.length < 33 || !image.subarray(0, 8).equals(pngMagic)) {
  throw new Error("art.png does not start with the PNG signature");
}
if (image.subarray(12, 16).toString("ascii") !== "IHDR") {
  throw new Error("art.png has no IHDR chunk in first position");
}
const width = image.readUInt32BE(16);
const height = image.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`art.png is ${width}x${height}, but the gate needs 1024x1024`);
}
if (image.length > 1048576) {
  throw new Error(`art.png is ${image.length} bytes, over the 1 MiB limit`);
}
// A whole PNG ends with the IEND chunk: a zero length field, then "IEND".
const tail = image.subarray(image.length - 12);
if (tail.readUInt32BE(0) !== 0 || tail.subarray(4, 8).toString("ascii") !== "IEND") {
  throw new Error("art.png does not end with a complete IEND chunk");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "entry.png");
writeFileSync(outPath, image);

const sha = createHash("sha256").update(image).digest("hex");
console.log(`copied art.png -> ${outPath} (${image.length} bytes, sha256 ${sha})`);
