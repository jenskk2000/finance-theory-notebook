// Short authored guides. These orient a learner to the original material;
// they are not a substitute for a full source-by-source lesson conversion.
export const moduleGuides = {
  '03': {
    question: 'What is a promised dollar worth when its payment date and interest rate change?',
    ideas: [
      ['Start with cash flows', 'A zero-coupon bond pays its face value once. A coupon bond pays periodic coupons plus principal at maturity. Price each dated payment with a discount factor appropriate to that date, then add the present values.'],
      ['Read the yield curve', 'A spot rate discounts one maturity. A forward rate describes a rate implied between future dates by today’s discount factors. Yield to maturity is the single rate that reproduces a bond price; it is not generally the rate for every cash flow.'],
      ['Measure sensitivity', 'Price and yield move in opposite directions. Duration approximates the percentage price change for a small yield move; convexity describes the curvature that the linear duration approximation misses. Defaultable corporate bonds add credit risk to the interest-rate question.']
    ],
    formula: 'Bond price = Σ couponₜ × discount factorₜ + face value × discount factorₜ₌T',
    example: 'A two-year bond with $5 annual coupons and $100 face value, discounted at a flat 5% annual rate, costs $5/1.05 + $105/1.05² = $100. A different term structure requires a separate factor for each payment.',
    check: 'Why is one yield to maturity insufficient to value every cash flow when spot rates differ by maturity?',
    practice: ['Questions 36–100', 15, 49], recitation: 'Recitation 2'
  },
  '04': {
    question: 'How can future dividends and growth opportunities support a stock price?',
    ideas: [
      ['Value distributions', 'A share is a claim on future distributions. The dividend discount model adds the present value of expected dividends; forecasts and discount rates both matter. A constant-growth shortcut requires growth below the required return.'],
      ['Separate earnings from cash paid out', 'Earnings per share are not dividends. Retained earnings can fund positive-NPV investments, but growth by itself does not create value when reinvestment earns less than its cost of capital.'],
      ['Use multiples carefully', 'A price-to-earnings ratio compresses growth, payout, risk, and accounting choices into one number. Comparing P/E ratios without those drivers can confuse cheapness with a lower-quality claim.']
    ],
    formula: 'Constant-growth DDM: P₀ = D₁ / (r − g), only when r > g',
    example: 'If next year’s dividend is $3, the required return is 8%, and perpetual growth is 2%, the model gives $3/(0.08−0.02) = $50 per share.',
    check: 'Can a firm increase earnings yet destroy shareholder value through reinvestment?',
    practice: ['Questions 101–136', 34, 64], recitation: 'Recitation 3'
  },
  '05': {
    question: 'How do prices today constrain a delivery price agreed for the future?',
    ideas: [
      ['Define the contract', 'A forward commits two parties to exchange an asset later at a price fixed now. A futures contract is standardized and marked to market, so gains and losses are settled along the way.'],
      ['Use replication', 'If storage, income, and financing are specified, buying the asset and financing it to delivery must be comparable to contracting for future delivery. An inconsistent price invites a cash-and-carry or reverse trade, subject to real trading frictions.'],
      ['Distinguish hedge from profit', 'A hedge changes exposure to future prices. A short futures position can offset an existing long exposure, but basis risk remains when the contract and the item being hedged differ.']
    ],
    formula: 'For a non-income asset with no storage cost: forward price F₀ = S₀(1 + r)ᵀ',
    example: 'With a $100 spot price and a one-year 5% financing rate, the simplified no-arbitrage delivery price is $105. Dividends or storage costs change this calculation.',
    check: 'Why does daily settlement make a futures contract operationally different from a forward?',
    recitation: 'Recitation 4'
  },
  '06': {
    question: 'How can an asymmetric payoff be built and priced?',
    ideas: [
      ['Draw the payoff first', 'A call pays max(Sₜ−K, 0); a put pays max(K−Sₜ, 0) at expiry. Profit also subtracts the premium paid. Keeping payoff and profit separate prevents a common sign error.'],
      ['Combine positions', 'A protective put adds a floor to a stock position. A covered call gives up upside above the strike in exchange for premium. Plot each leg before adding them.'],
      ['Replicate in a small model', 'In a one-period binomial tree, choose stock and risk-free holdings that match the option’s up and down payoffs. The same cost prices the option in that model; the result depends on its assumptions.']
    ],
    formula: 'Call payoff at expiry = max(Sₜ − K, 0)',
    example: 'A call with strike $100 has a $20 expiry payoff if the stock ends at $120. If the call cost $8, its profit before financing and fees is $12.',
    check: 'Can a call have a positive payoff while its buyer still loses money?',
    recitation: 'Recitation 5'
  },
  '07': {
    question: 'What does an average return hide about uncertainty?',
    ideas: [
      ['Specify the return', 'A holding-period return combines the price change with cash distributions and divides by the initial price. Arithmetic and compounded multi-period returns answer different questions.'],
      ['Describe a distribution', 'Expected return is a probability-weighted average, not a guarantee. Variance and standard deviation describe dispersion around that average but do not capture every feature of losses.'],
      ['Inspect evidence', 'Historical returns can display skew, fat tails, and changing volatility. A model fitted to a particular sample may not describe the next period or the impact of rare events.']
    ],
    formula: 'Holding-period return = (ending price + cash payout − starting price) / starting price',
    example: 'A $100 stock that ends at $106 and pays $2 returned 8% during the period. That observed 8% is one realization, not its expected return.',
    check: 'Do two investments with the same expected return necessarily have the same risk?'
  },
  '08': {
    question: 'When does combining risky assets reduce portfolio risk?',
    ideas: [
      ['Look beyond individual volatility', 'Portfolio return is a weighted average of asset returns. Portfolio variance also includes how assets move together, measured by covariance or correlation.'],
      ['Explore diversification', 'Holding imperfectly correlated assets can reduce volatility without reducing expected return in the same proportion. Correlation can change under stress, so historical co-movement is not a permanent guarantee.'],
      ['Find efficient choices', 'An efficient portfolio has no available alternative with both higher expected return and lower risk. The tangency portfolio maximizes the modeled reward-to-risk slope when a risk-free asset is available.']
    ],
    formula: 'For two assets: σₚ² = w²σ₁² + (1−w)²σ₂² + 2w(1−w)Cov(R₁,R₂)',
    example: 'Two equally weighted assets each have 20% volatility. If their correlation is zero, portfolio volatility is about 14.1%; if correlation is one, it remains 20%.',
    check: 'Which term in portfolio variance captures the benefit of imperfect correlation?',
    recitation: 'Recitation 6'
  },
  '09': {
    question: 'Which risk earns a return premium in a diversified market?',
    ideas: [
      ['Separate total risk and beta', 'CAPM relates expected excess return to market beta, a measure of exposure to market movements. Firm-specific risk can be diversified away in the model and does not command its own premium.'],
      ['Read the pricing line', 'The security market line begins at the risk-free rate and has slope equal to the expected market premium. A required return is a model output, not an observed future outcome.'],
      ['Test the assumptions', 'APT permits several systematic factors. Both approaches depend on how factors, portfolios, samples, and expected returns are estimated; empirical performance is part of the course discussion.']
    ],
    formula: 'CAPM: E[Rᵢ] = rᶠ + βᵢ(E[Rₘ] − rᶠ)',
    example: 'With a 3% risk-free rate, 6% expected market premium, and beta 1.2, CAPM implies 10.2% expected return.',
    check: 'Why can a volatile stock have a modest CAPM required return?',
    recitation: 'Recitation 7'
  },
  '10': {
    question: 'Which proposed investment adds value to a firm?',
    ideas: [
      ['Build incremental cash flows', 'Compare the firm with and without the project. Include opportunity costs and relevant side effects; exclude sunk costs. Keep financing decisions separate from operating cash flows when the chosen valuation method requires it.'],
      ['Apply NPV consistently', 'Discount incremental future cash flows at a rate matched to their risk and timing. Positive NPV means the modeled project exceeds its opportunity cost of capital.'],
      ['Check interactions and alternatives', 'Mutually exclusive projects, scale, timing, and real options can change the decision. IRR and payback may be useful summaries but can conflict with NPV under some cash-flow patterns.']
    ],
    formula: 'NPV = initial cash flow + Σ future incremental cash flowₜ / (1 + r)ᵗ',
    example: 'A $100 cost today followed by $60 at each of the next two year-ends has NPV = −100 + 60/1.10 + 60/1.10² ≈ $4.13 at a 10% rate.',
    check: 'Why should a cost already incurred before the decision be excluded from incremental NPV?',
    recitation: 'Recitation 8'
  },
  '11': {
    question: 'What does it mean for prices to reflect information?',
    ideas: [
      ['Define a testable claim', 'Market efficiency concerns how information is incorporated into prices. A surprising price move after new information is consistent with fast adjustment; predictability requires a carefully specified information set and trading rule.'],
      ['Beware joint tests', 'A return anomaly may indicate a pricing error, an incomplete risk model, data selection, or trading costs. Tests of efficiency usually also test a model of normal returns.'],
      ['Compare explanations', 'The original lecture discusses behavioral accounts and the adaptive markets hypothesis alongside rational-market accounts. These are interpretive frameworks, not a license to infer profitable trades from a chart alone.']
    ],
    formula: 'A useful test compares risk-adjusted returns after costs against a declared benchmark and information set.',
    example: 'A strategy discovered after examining thousands of patterns may look profitable in its discovery sample. Out-of-sample testing and realistic costs are needed before that observation supports a claim.',
    check: 'Why does an abnormal-return test depend on the benchmark model?'
  },
  '12': {
    question: 'How do valuation, risk, and investment decisions fit together?',
    ideas: [
      ['Value dated claims', 'Present value turns future cash flows into comparable values. Bonds, shares, forwards, and options differ in their cash-flow patterns and contingencies, so their models state different assumptions.'],
      ['Price risk', 'Return distributions, covariance, diversification, and factor models connect uncertainty to required returns. A discount rate must match the risk of the cash flow being valued.'],
      ['Make a decision', 'Capital budgeting applies valuation to incremental projects. Market-efficiency questions ask how much information is already reflected in prices and where a claimed advantage would come from.']
    ],
    formula: 'Decision chain: cash-flow forecast → risk-matched valuation → comparison with cost → decision',
    example: 'For a new project, forecast incremental cash flows, identify their risk, discount them consistently, and accept only if the resulting NPV is positive under the chosen objective.',
    check: 'What changes if a project’s cash flows become riskier while their expected amounts stay fixed?'
  }
};
