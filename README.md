# ZOID-NEWS-CYBERSECURITY-DISCORD-BOT-GENERATOR
Zoid News is a Discord bot that automatically posts the latest cybersecurity news every 6 hours, using BBC Technology as its main source.

Staying updated with cybersecurity trends is crucial. Not just for personal awareness but also for demonstrating genuine interest during interviews. As an IT student, I wanted a way for people in my Discord server to easily keep up with the latest developments and spark meaningful discussions around real-world cybersecurity events.

Purpose:
I built this bot to help students and tech enthusiasts stay informed and encourage conversations about the latest news in cybersecurity. This awareness can be particularly useful when preparing for interviews or technical discussions, where understanding current trends can set you apart.

--------------------------------------------------------------------------------------------------------------------
**Tech Stack:**
Language: Python
Libraries: discord.py, feedparser, dotenv, os
Scheduler: discord.ext.tasks (runs every 6 hours)
--------------------------------------------------------------------------------------------------------------------
Key Features:
Fetches the latest cybersecurity-related headlines from BBC Technology RSS feed
Automatically posts updates every 6 hours to a designated Discord channel (Cyber news)
Sends an alert message notifying the community that new articles have arrived
Uses Discord embeds for clean, visually appealing news cards
--------------------------------------------------------------------------------------------------------------------
Code Overview:
The main logic handles retrieving and filtering BBC news articles for cybersecurity topics. The task loop (lines 47–50) posts updates periodically and alerts users when fresh news arrives.
--------------------------------------------------------------------------------------------------------------------
