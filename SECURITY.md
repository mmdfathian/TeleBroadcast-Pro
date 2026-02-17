# Security Policy

## Supported Versions
We currently provide security updates and bug fixes for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| v1.0.x  | :white_check_mark: |
| < 1.0.0 | :x:                |

## Reporting a Vulnerability
**Important: Do not report security vulnerabilities through public GitHub issues.**

If you discover a security-related bug (e.g., credential leaking, session vulnerability), please report it privately:
1. Use the [Security Advisories](https://github.com/mmdfathian/TeleBroadcast-Pro/security/advisories/new) page on GitHub.
2. If you cannot access the page above, please contact the maintainer directly through the contact info provided on their GitHub profile.

## Safety Guidelines for Users
To ensure the safety of your Telegram account and personal data, please follow these rules:

1. **Keep Credentials Private:** Never share your `.env` file, `API_ID`, or `API_HASH` with anyone.
2. **Session Security:** The `.session` files created by Telethon are highly sensitive. If someone gets access to these files, they can control your Telegram account. **Never** upload these files to GitHub or any public cloud.
3. **Anti-Spam Awareness:** Telegram has strict anti-spam policies. Always use reasonable delays (e.g., 30+ seconds) between messages.
4. **Environment Security:** Ensure your `.env` is listed in your `.gitignore` to prevent accidental leaks.

## Disclaimer
The developers of TeleBroadcast-Pro are not responsible for any misused credentials, leaked session files, or banned accounts resulting from the use of this tool. Use it responsibly and at your own risk.
