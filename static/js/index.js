function printinfo() {
    $.ajax({
        type: "POST",
        url: "/random",
        dataType: "json",
        data:{"data": "xxxxxx"},
        success: function(msg)
         {
             console.log(msg);
             $("#display").text(msg.words);//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
};

function rand_word() {
    $.ajax({
         type: "POST",
         url: "/index",
         dataType: "json",
         data:{"words": 1},
         success: function(msg)
         {
            console.log(msg);
            $("#display").text("随机单词: " + msg.words);//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function prior_word() {
    $.ajax({
         type: "POST",
         url: "/prior_word",
         dataType: "json",
         data:{"words": 1},
         success: function(msg)
         {
            console.log(msg);
            $("#display").text("随机单词: " + msg.words);//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function next_word() {
    $.ajax({
         type: "POST",
         url: "/next_word",
         dataType: "json",
         data:{"words": 1},
         success: function(msg)
         {
            console.log(msg);
            $("#display").text("随机单词: " + msg.words);//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function show() {
    $.ajax({
         type: "POST",
         url: "/mean",
         dataType: "json",
         data:{"status": 1},
         success: function(msg)
         {
            console.log(msg);
            $("#meandisplay").text("单词意思: " + msg.means.mean);//注意显示的内容
            $("#explaindisplay").text("单词解释: " + msg.means.explain);//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function unshow() {
    $.ajax({
         type: "POST",
         url: "/mean",
         dataType: "json",
         data:{"status": 1},
         success: function(msg)
         {
            console.log(msg);
            $("#meandisplay").text(" ");//注意显示的内容
            $("#explaindisplay").text(" ");//注意显示的内容
         },
         error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function addright() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 1},
        success: function(msg)
        {
            console.log(msg);
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function delright() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 2},
        success: function(msg)
        {
            console.log(msg);
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function adderror() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 0},
        success: function(msg)
        {
            console.log(msg);
            $("#errorwords").text("不认识单词: " + msg.error_words);//注意显示的内容
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

function delerror() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 3},
        success: function(msg)
        {
            console.log(msg);
            $("#errorwords").text("不认识单词: " + msg.error_words);//注意显示的内容
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

// 不熟悉单词
function addunfamiliar() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 4},
        success: function(msg)
        {
            console.log(msg);
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar)
            $("#unfamiliarwords").text("不熟悉单词: " + msg.unfamiliar_words);//注意显示的内容
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

// 不熟悉单词
function delunfamiliar() {
    $.ajax({
        type: "POST",
        url: "/check",
        dataType: "json",
        data:{"status": 5},
        success: function(msg)
        {
            console.log(msg);
            $("#errorright").text("认识: " + msg.right + ", 不认识: " + msg.error + ", 不熟悉: " + msg.unfamiliar)
            $("#unfamiliarwords").text("不熟悉单词: " + msg.unfamiliar_words);//注意显示的内容
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

// 计算正确率
function calacc() {
    $.ajax({
        type: "POST",
        url: "/acc",
        dataType: "json",
        data:{"status": 0},
        success: function(msg)
        {
            console.log(msg);
            $("#accuracy").text("正确率: " + msg.acc);//注意显示的内容
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}

// 重制
function reset() {
    $.ajax({
        type: "POST",
        url: "/reset",
        dataType: "json",
        data:{"status": 0},
        success: function(msg)
        {
            console.log(msg);
            $("#display").text(" ");//注意显示的内容
            $("#meandisplay").text(" ");//注意显示的内容
            $("#explaindisplay").text(" ");//注意显示的内容
            $("#errorwords").text(" ");//注意显示的内容
            $("#errorright").text(" "); //注意显示的内容
            $("#unfamiliarwords").text(" "); //注意显示的内容
            $("#accuracy").text(" "); //注意显示的内容
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}