$(document).ready(function (evt) {
  Hasher.add('/clients/', clients__index);
  Hasher.add('/clients/new/', clients__new);
  Hasher.add('/clients/:id/', clients__show);
  Hasher.add('/clients/:id/edit/', clients__edit);
  Hasher.add('/clients/:id/delete/', clients__delete);


  Hasher.add('/projects/', projects__index);
  Hasher.add('/projects/new/', projects__new);
  Hasher.add('/projects/:id/', projects__show);
  Hasher.add('/projects/:id/edit/', projects__edit);
  Hasher.add('/projects/:id/delete/', projects__delete);

  Hasher.add('/tasks/', tasks__index);
  Hasher.add('/tasks/new/', tasks__new);
  Hasher.add('/tasks/:id/', tasks__show);
  Hasher.add('/tasks/:id/edit/', tasks__edit);
  Hasher.add('/tasks/:id/delete/', tasks__delete);

  Hasher.setup();
});
