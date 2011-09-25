$(document).ready(function (evt) {
  Hasher.add('/clients', clients__index);
  Hasher.add('/clients/new', clients__new);

  Hasher.setup();
});
