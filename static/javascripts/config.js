BASE_URL = "";

CLIENTS_INDEX = BASE_URL + "/clients/";
CLIENTS_NEW = BASE_URL + "/clients/new/"
CLIENTS_EDIT = function (id) { return BASE_URL + '/clients/' + id + '/edit/';};
CLIENTS_SHOW = function (id) { return BASE_URL + '/clients/' + id + '/';};

PROJECTS_INDEX = BASE_URL + "/projects/";
PROJECTS_NEW = BASE_URL + "/projects/new/"
PROJECTS_EDIT = function (id) { return BASE_URL + '/projects/' + id + '/edit/';};
PROJECTS_SHOW = function (id) { return BASE_URL + '/projects/' + id + '/';};

TASKS_INDEX = BASE_URL + "/tasks/";
TASKS_NEW = BASE_URL + "/tasks/new/"
TASKS_EDIT = function (id) { return BASE_URL + '/tasks/' + id + '/edit/';};
TASKS_SHOW = function (id) { return BASE_URL + '/tasks/' + id + '/';};


MODAL_OPTIONS = {
  backdrop: false,
  closeOnEscape: true,
  modal: true,
  show: true,
};
