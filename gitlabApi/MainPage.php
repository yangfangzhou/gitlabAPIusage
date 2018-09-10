<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>gitlab API</title>
<link href="css/css3.css" rel="stylesheet" type="text/css" />
<link href="css/button.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="css/mystyle.css">
<script type="text/javascript" src="jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="treegrow.js"></script>
<!-- gitlabApi 旨在为公司内部人员提供更方便的gitlab仓库管理,
对仓库操作的账户,分为gitlab管理员,项目经理,一般用户三种类型,
管理员拥有所有的gitlab相关权限,项目经理对其账户下包含的组和项目包含操作权限,
一般用户有申请加入组或项目的权限

对于一般用户,申请后会发送邮件给相关管理人员,由相关管理人员确认并点击链接进行权限提升

要查看到所有人员,项目和组,需要3级token权限
要查到账户下的人员,项目和组,需要1或2级token权限
要提升用户的权限或对项目或者组进行操作,需要2或3级token权限

用户申请组权限或者申请项目权限
-->
<canvas id='d1'  width="800" height="600" style="border:none  2px #ccc;z-index:-1;position:absolute;"></canvas>

<script>
var canvas=document.getElementById('d1');
var ctx= canvas.getContext('2d');
//初始化的树

function tree(){
    drawtree(ctx,500,600,100,-Math.PI / 2, 8, 12);
}

function treeclean(){
    setTimeout(function (){
    ctx.clearRect(0,0,800,600);
    return;
    },500)
}
function doUpload(){
         var formData = new FormData($( "#myForm" )[0]);
         htmlobj=$.ajax({
              url:'formHandle.php',
              type: 'POST',
              data: formData,
              async: true,
              cache: false,
              contentType: false,
              processData: false,
              //timeout:15000,
			  beforeSend:function(XMLHttpRequest){
			  //document.getElementById("demo").innerHTML="------------";
		 },
              success: function (returndata) {
				if($("#div3").html(htmlobj.responseText)){
                //document.getElementById("demo").style.display="none";
				}
              },
              error: function (returndata) {
              }
         });
}

$(document).ready(function(){
$(".flip0").click(function(){
    $(".panel0").slideToggle("slow");
  });
$(".flip1").click(function(){
    $(".panel1").slideToggle("slow");
  });
$(".flip2").click(function(){
    $(".panel2").slideToggle("slow");
  });
});

document.getElementById("d1").style.left=document.body.clientWidth -785 + 'px';
document.getElementById("d1").style.bottom=document.body.clientHeight  + 'px';
</script>
</head>

<body>
<div style="position:absolute;top:10px;left:600px">
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=7-cu&user_right_finally=<?php echo $admin_right;?>'">用户创建</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-cp&user_right_finally=<?php echo $normal_right;?>'">项目创建</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-cg&user_right_finally=<?php echo $normal_right;?>'">组创建</button>
<button class="btn5" type="button" style="float:left;display:none;" onclick="document.location.href='?parameter_number=3-du&user_right_finally=<?php echo $admin_right;?>'">用户删除</button>
<br>
<br>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=3-spm&user_right_finally=<?php echo $search_right;?>'">项目用户</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=3-sgp&user_right_finally=<?php echo $search_right;?>'">组内项目</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=3-sgm&user_right_finally=<?php echo $search_right;?>'">组内用户</button>
<br>
<br>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=4-tp&user_right_finally=<?php echo $normal_right;?>'">移动项目</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-cgm&user_right_finally=<?php echo $normal_right;?>'">add组用户</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-cpm&user_right_finally=<?php echo $normal_right;?>'">add项目用户</button>
<br>
<br>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-egm&user_right_finally=<?php echo $normal_right;?>'">edit项目用户</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=5-epm&user_right_finally=<?php echo $normal_right;?>'">edit组用户</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=4-rpm&user_right_finally=<?php echo $admin_right;?>'">rm项目用户</button>
<br>
<br>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=4-rgm&user_right_finally=<?php echo $admin_right;?>'">rm组用户</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=3-bu&user_right_finally=<?php echo $admin_right;?>'">用户封禁</button>
<button class="btn5" type="button" style="float:left;" onclick="document.location.href='?parameter_number=3-ubu&user_right_finally=<?php echo $admin_right;?>'">用户解封</button>
<br>
<br>
<div  style="float:left;width:150px;">
<div class="flip0" >
<button class="btn5" type="button"  onclick="tree();" >所有用户</button>
</div>

<?php
session_start();
$user_name = $_COOKIE['username'];
echo "1";
echo $user_name;
 ?>
<div class="panel0" style="display:none; width:150px;vertical-align:top;">
<?php


/*
  $conn = new mysqli('172.10.11.13:1337', 'gitlabApi', 'autoio_admin_yocto', 'gitlabApi');
   if (mysqli_connect_errno()) {
     echo 'Error: Could not connect to database.  Please try again later.';
     exit;
  }else{
    //echo 'connect success!';
    }
$res = "SELECT `user_right` from autoiouser where (user_name = '$user_name')";
$result = $conn->query($res);

$right_results = $result->fetch_array();
$result->close();

switch ($right_results[0])
{
case 1:
  $search_right = "1";
  $normal_right = "1";
  $admin_right = "1";
  break;
case 2:
  $search_right = "3";
  $normal_right = "3";
  $admin_right = "2";
  break;
case 3:
  $search_right = "3";
  $normal_right = "3";
  $admin_right = "3";
  break;
default:
  echo "用户cookie失效,请重新登录";
  return false;
}
*/
$user_right = 3;
$_SESSION['user_right'] = $user_right;
exec("python2.7 ./python/ToolsOfGitlab.py $user_right su",$output,$pyreturn);
$pyarray=explode(" ",$output[0]);
echo "<br>";
for($i = 0 ; $i < sizeof($pyarray)-1 ; $i++)
{
    //echo "<button class=\"btn7\" type=\"button\"  onclick=\"document.location.href='?user_name=$pyarray[$i]'\" >$pyarray[$i]</button>";
    echo "$pyarray[$i]";
    echo "<br>";
    }
if($_GET['user_name'])
{
    $_SESSION['user_name'] = $_GET['user_name'];
    $url="userPage.php";
    echo "<script LANGUAGE=\"javascript\">";
    echo "location.href='$url'";
    echo "</script>";
    }
?>
</div>
</div>

<div  style="float:left;width:150px;">
<div class="flip1" >
<button class="btn5" type="button"  onclick="treeclean();" >所有项目</button>
</div>

<div class="panel1" style="display:none; width:150px;vertical-align:top;">
<?php
exec("python2.7 ./python/ToolsOfGitlab.py $user_right sp",$output1,$pyreturn1);
$pyarray1=explode(" ",$output1[0]);
echo "<br>";
for($i = 0 ; $i < sizeof($pyarray1)-1 ; $i++)
{
    //echo "<button class=\"btn7\" type=\"button\"  onclick=\"location.href='projectPage.php'\" >$pyarray1[$i]</button>";
    echo "$pyarray1[$i]";
    echo "<br>";
    }
?>
</div>
</div>

<div  style="float:left;width:150px;">
<div class="flip2" >
<button class="btn5" type="button"  onclick="">所有组</button>
</div>

<div class="panel2" style="display:none; width:150px;vertical-align:top;">
<?php
exec("python2.7 ./python/ToolsOfGitlab.py $user_right sg",$output2,$pyreturn2);
$pyarray2=explode(" ",$output2[0]);
echo "<br>";
for($i = 0 ; $i < sizeof($pyarray2)-1 ; $i++)
{
    //echo "<button class=\"btn7\" type=\"button\"  onclick=\"location.href='groupPage.php'\" >$pyarray2[$i]</button>";
    echo "$pyarray2[$i]";
    echo "<br>";
    }
?>
</div>
</div>
</div>

<div style="position:absolute;top:10px;left:10px;width:550px;">
<form id= "myForm" action="" class="bootstrap-frm" enctype="multipart/form-data" method="post"
name="uploadfile" >
<h1>gitlab操作表
<span>请将参数在下表中填写并提交</span>
</h1>
<?php
$user_right_finally = $_GET['user_right_finally'];
if($_GET['parameter_number']) {
$j = explode("-",$_GET['parameter_number']);
$arr = array('spm' =>"搜索项目内的用户,<br>参数3是 路径/项目,<br>点击\"所有项目\"查看可用参数<br>",
             'sgm' =>"搜索组内的用户,<br>参数3是 组名称,<br>点击\"所有组\"查看可用参数<br>",
             'sgp' =>"搜索组内的项目,<br>参数3是 组名称,<br>点击\"所有组\"查看可用参数<br>",
             'tp' =>"移动项目到特定组,<br>参数3是 组名称,<br>参数4是 路径/项目,<br>点击\"所有组\" \"所有项目\"查看可用参数<br>",
             'cgm' =>"添加用户到特定组,<br>参数3是 组名称,<br>参数4是 用户名,<br>参数5是 用户的访问级别,<br>点击\"所有组\"  \"所有用户\"查看可用参数<br>",
             'cpm' =>"添加用户到特定项目,<br>参数3是 路径/项目,<br>参数4是 用户名,<br>参数5是 用户的访问级别,<br>点击\"所有项目\"  \"所有用户\"查看可用参数<br>",
             'egm' =>"编辑特定组的用户访问级别,<br>参数3是 组名称,<br>参数4是 用户名,<br>参数5是 用户的访问级别,<br>点击\"所有组\"  \"所有用户\"查看可用参数<br>",
             'epm' =>"编辑特定项目的用户访问级别,<br>参数3是 路径/项目,<br>参数4是 用户名,<br>参数5是 用户的访问级别,<br>点击\"所有项目\"  \"所有用户\"查看可用参数<br>",
             'rgm' =>"移除特定组内的用户,<br>参数3是 组名称,<br>参数4是 用户名,<br>点击\"所有组\"  \"所有用户\"查看可用参数<br>",
             'rpm' =>"移除特定项目内的用户,<br>参数3是 路径/项目,<br>参数4是 用户名,<br>点击\"所有项目\"  \"所有用户\"查看可用参数<br>",
             'bu' =>"封禁用户,<br>参数3是 用户名,<br>点击\"所有用户\"查看可用参数<br>",
             'ubu' =>"解封用户,<br>参数3是 用户名,<br>点击\"所有用户\"查看可用参数<br>",
             'du' =>"删除用户,<br>参数3是 用户名,<br>点击\"所有用户\"查看可用参数<br>",
             'cu' =>"创建新用户,<br>参数3是 用户名(中文/英文),<br>参数4是 用户登录名(英文),<br>参数5是 邮箱地址(参数必须包含@),<br>参数6是 用户密码(需要大于8位),<br>参数7是 是否能创建组(true/false),<br>点击\"所有用户\"查看可用参数<br>",
             'cg' =>"创建新组,<br>参数3是 组名(英文),<br>参数4是 组路径名(英文),<br>参数5是 组可见度<br>(0 for private, 10 for internal, 20 for public.),<br>点击\"所有用户\"查看可用参数<br>",
             'cp' =>"创建新项目,<br>参数3是 项目名(英文),<br>参数4是 项目路径名(英文),<br>参数5是 项目可见度<br>(0 for private, 10 for internal, 20 for public.),<br>点击\"所有用户\"查看可用参数<br>",
            );
?>

<?php
foreach($arr as $key => $value) {
    if ($key == $j[1])
        echo "$value"."<br>";
    }
?>
<?php    echo "<input type = \"hidden\"  name = \"parameter2\" value = \"$j[1]\" />";
         echo "<input type = \"hidden\"  name = \"parameter1\" value = \"$user_right_finally\" />";
    for($i = 3; $i <= $j[0]  ; $i++){
        echo "<span>参数$i:</span>";
        echo "<input type = \"text\"  name = \"parameter$i\" value = \"\" />";
        echo "<br>";
        }
}
?>
<input  type="button"  class="button" value="提交"   id="b01" onclick="doUpload()"/>
<br>
<br>
<div class="bootstrap-frm" style="width:400px" >
<h1>gitlab操作结果
<span>提交结果如下</span>
</h1>
<div id = "div3">
</div>
</div>
</div>

</body>
</html>
