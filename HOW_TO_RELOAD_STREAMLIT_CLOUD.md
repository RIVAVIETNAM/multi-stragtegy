# How to Reload Streamlit Cloud App

## Problem
Your export shows all zeros because the Streamlit Cloud app hasn't deployed the latest code yet.

## Solution: Reboot the App

### Method 1: From Streamlit Cloud Dashboard

1. **Go to**: https://share.streamlit.io/
2. **Find your app**: `multi-stragtegy-vnteam10`
3. **Click the 3-dot menu** (⋮) on your app
4. **Select**: "Reboot app"
5. **Wait** for deployment (usually 1-2 minutes)
6. **Check status**: Green dot = ready

### Method 2: From the App Itself

1. **Open your app**: https://multi-stragtegy-vnteam10.streamlit.app/
2. **Click** the hamburger menu (☰) in top-right
3. **Select**: "Manage app"
4. **Click**: "Reboot app"
5. **Wait** for the green checkmark

## Verify the Fix

After rebooting:

1. Go to your app
2. Load sample data
3. Run backtest on "Bollinger Bands"
4. You should see:
   - **Signals**: 2 buy, 19 sell
   - **Trades**: 4 (NOT zero!)
   - **Return**: Around +21%

## Why This Happened

- You pushed code at ~08:09 (latest fix)
- Your export was at 01:10 (before fix)
- Streamlit Cloud auto-deploys but may take time
- Manual reboot forces immediate deployment

## If Still Shows Zero After Reboot

1. **Check Logs**:
   - Go to app → Manage app → Logs
   - Look for "BUY at..." messages
   - If no BUY messages, there might be a different issue

2. **Clear Cache**:
   - In app, press `C` key
   - Select "Clear cache"
   - Try backtest again

3. **Check Git**:
   ```bash
   git log --oneline -n 1
   ```
   Should show: "fix: Fix backtest engine to correctly calculate shares..."

## Expected Results for Sample Data (500 days)

| Strategy | Trades | Return | Notes |
|----------|--------|--------|-------|
| MACD Crossover | ~148 | -93% | Many whipsaw trades |
| RSI Mean-Reversion | 0 | 0% | No RSI crossovers in data |
| Bollinger Bands | 4 | +21% | **Best performer!** |
| SMA Crossover | 0 | 0% | Windows too long for data |

---

**Last Updated**: 2025-12-24 08:10

