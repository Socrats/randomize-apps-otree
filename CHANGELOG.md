# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 29-01-2025
### Added
- **Support for Wait Pages**: Participants will now wait on a wait page until `PLAYERS_PER_GROUP` reach the wait page through different randomized apps.
- **Support for Mixed Randomization**: Instead of fully randomizing all apps, users can now specify which apps to randomize by placing them between `begin_randomize_apps_otree` and `end_randomize_apps_otree`.
- **Improved Page Navigation Handling**: `_increment_index_in_pages` has been overridden to ensure proper iteration through all pages, handling cases where the next app may appear earlier in oTree’s internal page index.
- **New App Randomization Structure**:
  - Use `begin_randomize_apps_otree` and `end_randomize_apps_otree`, defining the range of apps to randomize.
- **Example configurations** to reflect the new randomization structure, including:
  - `randomize_apps`: Fully randomizes apps.
  - `randomize_apps_with_wait_page`: Includes a wait page inside the randomized sequence.
  - `mix_randomize_apps`: Partially randomizes only certain apps, keeping others fixed.

---

## 🔄 How to Upgrade
1. Update your `app_sequence` configurations to use `begin_randomize_apps_otree` and `end_randomize_apps_otree` instead of `randomize-app-otree`.
2. If using wait pages, ensure your app logic accounts for players reaching the wait page at different times.

---

## 📌 Notes
- There are **five test apps**: `test_app1`, `test_app2`, `test_app3`, `test_app4`, and `test_app5`.
- To ensure compatibility, test your updated `app_sequence` before deployment.
- If you encounter issues, review how `_increment_index_in_pages` affects page iteration.
