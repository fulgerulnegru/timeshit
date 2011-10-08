BASE_URL = "";

CLIENTS_INDEX = BASE_URL + "/clients/";
CLIENTS_NEW = BASE_URL + "/clients/new/"
CLIENTS_EDIT = function (id) { return BASE_URL + '/clients/' + id + '/edit/';};
CLIENTS_SHOW = function (id) { return BASE_URL + '/clients/' + id + '/';};

MODAL_OPTIONS = {
  backdrop: true,
  closeOnEscape: true,
  modal: true,
  show: true,
};
