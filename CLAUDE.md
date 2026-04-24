# Project: [KMB-Skills]

## How to Run
- Install: `npm install`
- Dev server: `npm run dev` (port 3000)
- Tests: `npm test`
- Build: `npm run build`
- Required env vars: `DATABASE_URL`, `API_KEY` (see .env.example)

## Code Style
- TypeScript strict mode — no `any` types
- Use named exports, not default exports
- All async functions must handle errors with try/catch
- Components go in `/src/components`, hooks in `/src/hooks`

## Do Not Touch
- `/legacy/` — old code, do not refactor
- `/vendor/` — third-party, not ours
- `config/prod.json` — production config, never edit directly

## Current Priorities
- Working on: user authentication flow
- Blocked by: API rate limiting issue in `/src/api/client.ts`
- Next up: dashboard performance improvements
