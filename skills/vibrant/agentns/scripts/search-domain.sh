#!/bin/bash
# Search domain availability across 20 TLDs
# Usage: ./search-domain.sh <domain-name>

set -e

DOMAIN_NAME="$1"

if [ -z "$DOMAIN_NAME" ]; then
    echo "Usage: $0 <domain-name>"
    echo "Example: $0 myagent"
    exit 1
fi

echo "🔍 Searching availability for: $DOMAIN_NAME"
echo ""

# Search via AgentNS API
RESPONSE=$(curl -s -X POST https://agentns.xyz/domains/search \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$DOMAIN_NAME\"}")

# Parse and display results
echo "$RESPONSE" | jq -r '.results[] | "\(.domain) - Available: \(.available) - Price: $\(.price_usdc) USDC"'

echo ""
echo "💡 To register, visit: https://agentns.xyz"
echo "📖 Agent integration: https://agentns.xyz/howtoagents.md"
