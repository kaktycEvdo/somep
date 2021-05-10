//подключение к дб, закидывание в таблицу ссылки если нет совпадения в названии, в остальном обратно ++ сделать маленькую страницу авторизации и ссылкой на регистрацию

const mysql = require("mysql2");

const connection = mysql.createConnection({
    host: "127.0.0.1",
    user: "root",
    database: "db",
    password: ""
});

connection.connect(function(err){
    if (err) {
      return console.error("Ошибка: " + err.message);
    }
    else{
      console.log("Подключение к серверу MySQL успешно установлено");
    }
});

connection.query(
    'SELECT * FROM `links` WHERE `username` = '+sessionStorage.getItem('un')+' AND `password` ='+sessionStorage.getItem('pswrd'),
    function(err, results, fields) {
        function getItems(unt, pswrdt) {
            sessionStorage.setItem('un', unt.content)
            sessionStorage.setItem('pswrd', pswrdt.content);
        }

        //добавление ссылки на css-файл в <head>, то бишь добавление стиля
        css = document.createElement('link')
        css.href = 'style.css'
        document.head.appendChild(css)

        if(results==null){ //если результатов не нашлось, то есть не записаны в сессию пароль и имя пользователя
            //создание формы
            let form = document.createElement('form');

            //создание элементов формы: ввод имени пользователя, пароль и кнопка отправки данных
            form.method = 'POST';
            let untext = document.createElement('input')
            untext.type = 'text';
            let pswrdtext = document.createElement('input')
            pswrdtext.type = 'password';
            let submit = document.createElement('input')
            submit.type = 'submit';
            
            form.onsubmit = getItems(untext, pswrdtext);

            //добавление элементов выше в форму и добавление формы в body
            form.appendChild(untext);
            form.appendChild(pswrdtext);
            form.appendChild(submit);
            document.body.appendChild(form);
        }
        else{
            let form = document.createElement('form');
            // connection.execute('INSERT INTO links (link) VALUE '+document.location.toString())
        }
        if (err) {
        return console.log("Ошибка: " + err.message);
        }
    console.log(results); // results contains rows returned by server
    console.log(fields); // fields contains extra meta data about results, if available
    }
);

connection.end(function(err) {
    if (err) {
        return console.log("Ошибка: " + err.message);
    }
});