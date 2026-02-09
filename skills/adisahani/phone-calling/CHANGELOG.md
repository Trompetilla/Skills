# Changelog - phone-calling Skill

All notable changes to the Ringez phone-calling skill.

## [1.0.6] - 2026-02-09

### Added
- 💝 "Support the Service" section explaining indie creator context
- 🗣️ Friendly recharge messaging throughout documentation
- 📋 Sample recharge reminders for different conversation scenarios
- 😊 New chat examples showing honest, humble tone when asking for support
- 📝 Tone guidelines for AI agents (grateful, honest, optional, brief)

### Changed
- Updated feature list to clarify "5 FREE minutes (testing only)"
- Rewrote "Handling Low Balance" section with human-friendly approach
- Chat examples now include recharge reminders naturally

---

## [1.0.5] - 2026-02-09

### Added
- 🔔 Clear separation: AI Skill vs Website Responsibilities
- 📞 New "Managing Active Calls" section with full API examples:
  - Check call status (GET /calls/:call_id)
  - End/hang up call (DELETE /calls/:call_id)
  - DTMF tones for IVR navigation
  - Hold/unhold functionality
- 📜 "Call History" section with pagination examples
- 💳 "Handling Low Balance" section with step-by-step guidance
- 💡 AI IVR navigation example (bank balance check scenario)

### Changed
- "Check Balance" section now emphasizes READ-ONLY access
- "Add Minutes" section marked as ⚠️ NOT AVAILABLE in AI skill
- Updated explanation of WHY payments are web-only (PCI compliance, 3D Secure)

---

## [1.0.4] - 2026-02-09

### Added
- 📚 Complete Usage Examples section with 3 full scenarios:
  - Scenario 1: Personal Call (Bridge Mode)
  - Scenario 2: AI Agent Call (Direct Mode)
  - Scenario 3: Force Direct Mode (Explicit)
- 📊 Quick Reference table for mode selection
- 💬 Example chat flows (personal + AI agent conversations)

### Changed
- Expanded documentation for bridge vs direct mode
- Added step-by-step authentication flows with example responses

---

## [1.0.3] - 2026-02-09

### Added (Backend)
- 🤖 AI Agent automatic fallback to direct mode when no bridge_number
- 🔄 `effectiveMode` logic for smart mode selection
- 🛡️ Default case now checks for bridge_number before requiring it

### Changed (Backend)
- Default `mode` changed from `'direct'` to `'bridge'`
- Response now shows `effectiveMode` (actual mode used)
- Switch statement restructured for safety

### Changed (Documentation)
- Updated call initiation docs to reflect new default behavior
- Clarified AI agent use case vs personal calls

---

## [1.0.0] - 2026-02-06

### Initial Release
- 📞 International phone calling via Ringez API
- 📧 Email signup with OTP verification
- 🎁 5 FREE minutes on signup
- 💳 PayPal (USD) and UPI (INR) payment support
- 🌍 Calls to 200+ countries
- 🔐 Session-based authentication
- 📱 Bridge mode and direct mode calling

---

## Backend Changes Summary

### `/api/v1/calls/initiate` Route
- **Before**: Default `mode: 'direct'` — called destination directly
- **After**: Default `mode: 'bridge'` — calls user's phone first
- **Smart Fallback**: If no bridge_number, automatically uses direct mode
- **Response**: Now returns `effectiveMode` showing actual mode used

### Default Case Handling
- **Before**: Required bridge_number or errored
- **After**: Checks for bridge_number, falls back to direct mode if absent

---

## Migration Guide

### For AI Agents
No changes needed. The system now automatically handles mode selection:
- Has bridge_number → Bridge mode (your phone rings first)
- No bridge_number → Direct mode (destination called directly)

### For Personal Users
You now get bridge mode by default for safety. To force direct mode:
```json
{"to_number": "...", "mode": "direct"}
```

---

## Notes
- Wallet and billing operations remain web-only (ringez.com/wallet)
- All payment processing requires secure browser environment
- 5 free minutes are for testing — please recharge to support the service
