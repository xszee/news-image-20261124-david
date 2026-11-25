import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(here, "art.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const targetPath = join(outDir, "entry.png");

if (!existsSync(sourcePath)) {
  throw new Error(`missing artwork next to this script: ${sourcePath}`);
}

const picture = readFileSync(sourcePath);

const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (picture.length < 33 || !picture.subarray(0, 8).equals(pngMagic)) {
  throw new Error("art.png is not a PNG file (bad magic bytes)");
}
if (picture.subarray(12, 16).toString("ascii") !== "IHDR") {
  throw new Error("art.png has no IHDR chunk where one is expected");
}

const width = picture.readUInt32BE(16);
const height = picture.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`art.png must be 1024x1024, got ${width}x${height}`);
}

const oneMiB = 1024 * 1024;
if (picture.length > oneMiB) {
  throw new Error(`art.png is ${picture.length} bytes, over the 1 MiB limit`);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(targetPath, picture);

const digest = createHash("sha256").update(picture).digest("hex");
console.log(`entry written: ${targetPath}`);
console.log(`bytes: ${picture.length}`);
console.log(`sha256: ${digest}`);
