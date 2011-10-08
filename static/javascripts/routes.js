$(document).ready(function (evt) {
  Hasher.add('/clients/', clients__index);
  Hasher.add('/clients/new/', clients__new);
  Hasher.add('/clients/:id/', clients__show);
  Hasher.add('/clients/:id/edit/', clients__edit);
  Hasher.add('/clients/:id/delete/', clients__delete);

  Hasher.setup();
});
