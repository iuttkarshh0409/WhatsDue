document.addEventListener('DOMContentLoaded', () => {
  const editButtons = document.querySelectorAll('.edit-task');
  const deleteButtons = document.querySelectorAll('.delete-task');

  editButtons.forEach(button => {
    button.addEventListener('click', () => {
      alert('Edit functionality coming soon!');
      // Future: Implement edit modal or redirect to edit form
    });
  });

  deleteButtons.forEach(button => {
    button.addEventListener('click', () => {
      if (confirm('Are you sure you want to delete this task?')) {
        alert('Delete functionality coming soon!');
        // Future: Send DELETE request to backend
      }
    });
  });
});