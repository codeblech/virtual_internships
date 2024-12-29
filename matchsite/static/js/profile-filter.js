document.addEventListener("DOMContentLoaded", function () {
  const filterForm = document.getElementById("profile-filter-form");
  const profileCards = document.querySelectorAll(".profile-card");

  function filterProfiles() {
    const roleFilter = document.getElementById("role-filter").value;
    const skillFilter = document.getElementById("skill-filter").value.toLowerCase();
    const searchQuery = document.getElementById("search-query").value.toLowerCase();

    profileCards.forEach((card) => {
      const role = card.dataset.role;
      const skills = card.dataset.skills.toLowerCase();
      const username = card.querySelector("h3").textContent.toLowerCase();
      const bio = card.querySelector("p").textContent.toLowerCase();

      const matchesRole = roleFilter === "all" || role === roleFilter;
      const matchesSkill = !skillFilter || skills.includes(skillFilter);
      const matchesSearch = !searchQuery || username.includes(searchQuery) || bio.includes(searchQuery);

      card.style.display = matchesRole && matchesSkill && matchesSearch ? "block" : "none";
    });
  }

  filterForm.addEventListener("submit", function (e) {
    e.preventDefault();
    filterProfiles();
  });

  // Real-time filtering
  filterForm.querySelectorAll("select, input").forEach((element) => {
    element.addEventListener("input", filterProfiles);
  });
});
