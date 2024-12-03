import { describe, it, expect } from 'bun:test';
import sum from './index.js';

describe('sum', () => {
  it('should return the correct sum of two positive numbers', () => {
    expect(sum(5, 3)).toBe(8);
  });

  it('should return 0 when the first argument is not a number', () => {
    expect(sum('a', 3)).toBe(0);
  });

  it('should return 0 when the second argument is not a number', () => {
    expect(sum(5, 'b')).toBe(0);
  });

  it('should return 0 when either argument is negative', () => {
    expect(sum(-5, 3)).toBe(0);
    expect(sum(5, -3)).toBe(0);
    expect(sum(-5, -3)).toBe(0);
  });

  it('should return 0 when both arguments are not numbers', () => {
    expect(sum('a', 'b')).toBe(0);
  });

  it('should return the correct sum for zero as an argument', () => {
    expect(sum(0, 5)).toBe(5);
    expect(sum(5, 0)).toBe(5);
    expect(sum(0, 0)).toBe(0);
  });
});
