import { reactive, computed } from "vue";
import { defineStore } from "pinia";

export const useCuctomerStore = defineStore("customer", () => {
  // const main_api_url = "http://0.0.0.0:8000" + "/";
  const main_api_url = "http://localhost:8000" + "/";
  // const main_api_url = "/";

  const media_url = main_api_url + "media/";
  // const media_url  = "/usr/src/app/media/"
  const urls = {
    main: main_api_url,
    main_img_url: media_url + "default_img/pizza_title_main.jpg",
    // login: main_api_url + "api-token-auth/",
    login: main_api_url + "api-users/login/",
    registr: main_api_url + "api-users/registrations/",
    create_order: main_api_url + "api-order/create/",
  };
  function get_url(url_name) {
    return urls[url_name];
  }

  const user_data = reactive({
    auth: false,
    email: null,
    nickname: null,
    phone_number: null,
    birthday: null,
    user_token: null,
    last_address: null,
  });

  const check_auth = () => {
    return user_data.auth === true;
  };
  function get_user_data() {
    _get_extra_data_from_local_storage();
    return user_data;
  }
  function _get_extra_data_from_local_storage() {
    user_data.nickname = localStorage.getItem("nickname");
    user_data.phone_number = localStorage.getItem("phone_number");
    user_data.last_address = localStorage.getItem("last_address");
  }
  function get_config_to_order() {
    const config = {
      headers: {
        Authorization: "Token" + " " + user_data.user_token,
      },
    };
    return config;
  }
  function add_data_to_local_storage_after_login(email, nickname, user_token) {
    localStorage.setItem("nickname", nickname);
    localStorage.setItem("email", email);
    localStorage.setItem("user_token", user_token);
    console.log("save data to local storage after login");
  }
  function add_data_to_local_storage_after_order(
    nickname,
    phone_number,
    last_address
  ) {
    localStorage.setItem("nickname", nickname);
    localStorage.setItem("phone_number", phone_number);
    localStorage.setItem("last_address", last_address);
    console.log("save data to local storage after order");
  }

  function add_data_to_pinia(email, nickname, user_token) {
    user_data.auth = true;
    user_data.email = email;
    user_data.nickname = nickname;
    user_data.user_token = user_token;
  }
  function remove_data_from_pinia() {
    user_data.auth = false;
    user_data.email = null;
    user_data.nickname = null;
    user_data.user_token = null;
  }
  function load_user_data_from_local_storege() {
    const email = localStorage.getItem("user_email");
    const user_token = localStorage.getItem("user_token");
    if ((email, user_token)) {
      const nickname = localStorage.getItem("user_nickname");
      add_data_to_pinia(email, nickname, user_token);
      console.log("load data from local storage to pinia");
    }
  }

  function save_data_after_login(email, user_token) {
    const nickname = "";
    add_data_to_local_storage_after_login(email, nickname, user_token);
    add_data_to_pinia(email, nickname, user_token);
  }

  function save_data_after_registration(email, nickname, user_token) {
    add_data_to_local_storage_after_login(email, nickname, user_token);
    add_data_to_pinia(email, nickname, user_token);
  }

  function logout() {
    remove_data_from_pinia();
    console.log("logout");
  }

  return {
    user_data,
    check_auth,
    get_url,
    save_data_after_login,
    save_data_after_registration,
    logout,
    load_user_data_from_local_storege,
    get_user_data,
    add_data_to_local_storage_after_order,
    get_config_to_order,
  };
});
