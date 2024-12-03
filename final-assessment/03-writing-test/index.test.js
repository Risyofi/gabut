import { describe, it, expect } from 'bun:test';
import { sum } from './index.js';

describe('sum', () => {
  it('harus mengembalikan jumlah yang benar dari dua angka positif', () => {
    expect(sum(2, 3)).toBe(5);
  });

  it('harus mengembalikan jumlah yang benar dari dua angka negatif', () => {
    expect(sum(-2, -3)).toBe(-5);
  });

  it('harus mengembalikan nol jika kedua angka adalah nol', () => {
    expect(sum(0, 0)).toBe(0);
  });

  it('harus mengembalikan jumlah yang benar dari satu angka positif dan satu angka negatif', () => {
    expect(sum(5, -3)).toBe(2);
  });
});
