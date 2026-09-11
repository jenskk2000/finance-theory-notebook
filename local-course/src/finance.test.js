import { describe, expect, it } from 'vitest';
import { annuityPV, effectiveAnnualRate, fv, growingPerpetuityPV, npv, realRate } from './finance.js';

describe('present value calculations', () => {
  it('matches the lecture lighting project', () => expect(npv([-230000, 90000, 90000, 90000], .04)).toBeCloseTo(19758.19, 2));
  it('compounds 1000 for one year', () => expect(fv(1000, .1, 1)).toBe(1100));
  it('values an ordinary annuity', () => expect(annuityPV(100000, .1, 20)).toBeCloseTo(851356.37, 1));
  it('handles a zero-rate annuity', () => expect(annuityPV(100, 0, 5)).toBe(500));
  it('values the recitation scholarship perpetuity', () => expect(growingPerpetuityPV(1_020_000, .05, .02)).toBeCloseTo(34_000_000, 0));
  it('rejects a non-convergent growing perpetuity', () => expect(() => growingPerpetuityPV(100, .03, .03)).toThrow());
  it('converts APR to EAR', () => expect(effectiveAnnualRate(.045, 12)).toBeCloseTo(.04594, 5));
  it('converts nominal to real rates', () => expect(realRate(.05, .02)).toBeCloseTo(.029412, 5));
});
