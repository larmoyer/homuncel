# Maintainer setup (one-time)

## Done (as of last check)

- Repo is **public**: https://github.com/larmoyer/homuncel
- **Discussions** enabled (GitHub default categories present)
- **Private vulnerability reporting** enabled (CONTACT / SECURITY)

## Categories (API cannot create/rename these)

GitHub only exposes category management in the UI. Defaults already match the intended structure:

| Name (default) | Slug | Role |
|----------------|------|------|
| Announcements | `announcements` | Releases, policy |
| Q&A | `q-a` | Questions / how-to (answerable) |
| Ideas | `ideas` | Product ideas |
| Show and tell | `show-and-tell` | Setups, demos |

Optional UI polish (not required — docs link to the slugs above):

1. Open https://github.com/larmoyer/homuncel/discussions
2. Click the gear / **Edit categories** (or **Categories** in the Discussions sidebar)
3. Rename **Q&A** → **Questions** if you prefer that label
4. Delete unused defaults (**General**, **Polls**) if you want a cleaner list

You can delete this file after you are happy with categories. You may also drop Administration from the PAT once settings are stable.
