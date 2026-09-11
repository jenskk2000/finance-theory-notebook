const moduleRows = [
  ['01','Introduction and Course Overview','Finance as decisions across time and uncertainty','mapped'],
  ['02','Present Value Relations','Discounting, compounding, annuities, perpetuities and inflation','pilot'],
  ['03','Fixed-Income Securities','Bond prices, yield curves, duration and immunization','mapped'],
  ['04','Equities','Dividend discount models, earnings and growth opportunities','mapped'],
  ['05','Forward and Futures Contracts','No-arbitrage pricing, carry and hedging','mapped'],
  ['06','Options','Calls, puts, strategies, replication and option pricing','mapped'],
  ['07','Risk and Return','Expected returns and measures of risk','mapped'],
  ['08','Portfolio Theory','Covariance, diversification and efficient portfolios','mapped'],
  ['09','The CAPM and APT','Systematic risk, beta, equilibrium returns and factor pricing','mapped'],
  ['10','Capital Budgeting','Project cash flows, NPV, IRR and real options','mapped'],
  ['11','Efficient Markets','Market efficiency, evidence and limits of predictability','mapped'],
  ['12','Course Summary','Connect valuation, risk and corporate decisions','mapped']
];
const moduleAssets = [
  ['introduction.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/introduction-and-course-overview/','https://www.youtube.com/watch?v=HdHlfiOAJyE'],
  ['present-value-slides.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/present-value-relations/','https://www.youtube.com/watch?v=U03Md5enU-0'],
  ['fixed-income.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/fixed-income-securities/','https://www.youtube.com/watch?v=hyc8h5T76BE'],
  ['equities.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/equities/','https://www.youtube.com/watch?v=cny-1yDbQno'],
  ['forwards-futures.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/forward-and-futures-contracts/','https://www.youtube.com/watch?v=i_pLF9J3QPE'],
  ['options.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/options/','https://www.youtube.com/watch?v=IwA7nVEwqto'],
  ['risk-return.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/risk-and-return/','https://www.youtube.com/watch?v=Q2qjnLO3I_M'],
  ['portfolio-theory.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/portfolio-theory/','https://www.youtube.com/watch?v=tL7Lcl90Sc0'],
  ['capm-apt.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/the-capm-and-apt/','https://www.youtube.com/watch?v=z2oQe6B1Qa4'],
  ['capital-budgeting.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/capital-budgeting/','https://www.youtube.com/watch?v=JE80wLNIhjE'],
  ['efficient-markets.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/efficient-markets/','https://www.youtube.com/watch?v=sMKQywwkIjQ'],
  ['course-summary.pdf','https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/course-summary/','https://www.youtube.com/watch?v=P03PfYgNjmw']
];
export const modules = moduleRows.map(([number,title,concept,status],i) => ({number,title,concept,status,pdf:`/sources/${moduleAssets[i][0]}`,ocw:moduleAssets[i][1],video:moduleAssets[i][2]}));

export const lessons = [
  { id:'cashflows', number:'01', title:'Cash flows are dated currencies', summary:'Turn an asset into a timeline and choose a common valuation date.', anchor:'slides 3–13' },
  { id:'discounting', number:'02', title:'Move money through time', summary:'Derive present and future value from the opportunity cost of capital.', anchor:'slides 14–21' },
  { id:'streams', number:'03', title:'Value many cash flows', summary:'Use the NPV operator and make a project decision.', anchor:'slides 10–20' },
  { id:'annuities', number:'04', title:'Annuities and perpetuities', summary:'Recognize and derive finite, infinite, and growing cash-flow patterns.', anchor:'slides 22–27' },
  { id:'compounding', number:'05', title:'Compounding conventions', summary:'Convert APR to EAR before moving money across years.', anchor:'slides 28–29' },
  { id:'inflation', number:'06', title:'Inflation: real and nominal value', summary:'Keep cash flows and discount rates in consistent units.', anchor:'slides 30–35' }
];

export const introSections = [
  {id:'intro-purpose',number:'01',title:'What finance is',summary:'See finance as disciplined decisions about money.'},
  {id:'intro-system',number:'02',title:'The financial system',summary:'Follow funds among households, firms, intermediaries, and markets.'},
  {id:'intro-decisions',number:'03',title:'Value, manage, decide',summary:'Separate objectives, valuations, and decisions.'},
  {id:'intro-information',number:'04',title:'Price discovery',summary:'Experience how information changes bids and valuations.'},
  {id:'intro-principles',number:'05',title:'Time, risk, and six principles',summary:'Learn the course’s modeling assumptions and qualifications.'},
  {id:'intro-roadmap',number:'06',title:'Course roadmap',summary:'Connect the twelve modern modules to the original four-part arc.'}
];

export const sources = [
  { kind:'Lecture slides', title:'Present Value Relations · slides 1–36', href:'/sources/present-value-slides.pdf', detail:'MIT 15.401, Lectures 2–3' },
  { kind:'Recitation', title:'Recitation 1 · Present Value', href:'/sources/present-value-recitation.pdf', detail:'Concept review and four worked examples' },
  { kind:'Original practice', title:'Problems 1–35 · question pages 7–14', href:'/sources/problem-sets.pdf#page=7', detail:'The complete original PV problem set' },
  { kind:'Original solutions', title:'Solutions 1–35 · pages 42–48', href:'/sources/problem-sets.pdf#page=42', detail:'MIT solutions; compare after attempting' },
  { kind:'Transcript', title:'Present Value Relations I transcript', href:'/sources/session-02-transcript.pdf', detail:'Lecture session 2' },
  { kind:'Transcript', title:'Present Value Relations II transcript', href:'/sources/session-03-transcript.pdf', detail:'Lecture session 3' },
  { kind:'Transcript', title:'Present Value Relations III transcript', href:'/sources/session-04-transcript.pdf', detail:'Session 4, first segment' }
];

export const introSources = [
  {kind:'Lecture slides',title:'Introduction and Course Overview · slides 1–20',href:'/sources/introduction.pdf#page=2',detail:'MIT 15.401, Lecture 1'},
  {kind:'Transcript',title:'Lecture 1 transcript',href:'/sources/session-01-transcript.pdf',detail:'Complete local transcript'},
  {kind:'Course outline',title:'Course outline by topic',href:'/sources/course-outline.pdf#page=1',detail:'Original four-part curriculum'},
  {kind:'Video',title:'Lecture 1 recording',href:'/media/session-01.mp4',detail:'Complete local MIT recording'}
];

export const sourceNote = 'Original course materials: MIT OpenCourseWare 15.401 Finance Theory I, Fall 2008, Andrew W. Lo. Authored explanations and interactions in this pilot are adaptations for local study. MIT materials retain their stated CC BY-NC-SA 4.0 license and credits.';
