export const fv = (pv, rate, periods) => pv * (1 + rate) ** periods;
export const pv = (cash, rate, period) => cash / (1 + rate) ** period;
export const npv = (cashflows, rate) => cashflows.reduce((total, cash, period) => total + pv(cash, rate, period), 0);
export const annuityPV = (cash, rate, periods) => rate === 0 ? cash * periods : cash / rate * (1 - 1 / (1 + rate) ** periods);
export const growingPerpetuityPV = (cashNextPeriod, rate, growth) => {
  if (rate <= growth) throw new Error('The discount rate must exceed growth for a finite value.');
  return cashNextPeriod / (rate - growth);
};
export const effectiveAnnualRate = (apr, compounds) => (1 + apr / compounds) ** compounds - 1;
export const realRate = (nominal, inflation) => (1 + nominal) / (1 + inflation) - 1;

export function formatMoney(value, digits = 0) {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: digits }).format(value);
}
