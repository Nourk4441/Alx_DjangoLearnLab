## Permissions and Groups Setup

- **Custom Permissions**: Added `can_view`, `can_create`, `can_edit`, `can_delete` to the `Book` model.
- **Groups**:
  - `Viewers`: Can view books.
  - `Editors`: Can view, create, and edit books.
  - `Admins`: Can perform all actions.
- **Enforced Permissions**:
  - Used `@permission_required` in views for access control.
- **Testing**:
  - Manually tested with test users in various groups.
  - Automated tests are available in `tests.py`.