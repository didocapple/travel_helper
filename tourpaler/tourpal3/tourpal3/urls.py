﻿#coding utf-8
from django.conf.urls import include, url
from django.contrib import admin
from tourpal.views import *
urlpatterns = [
    url(r'^$', home),
    url(r'^home/$',home),
    url(r'^register/$',register),
    url(r'^login/$',login),
    url(r'^loginout/$',loginout),
    url(r'^user/find/(?P<team_id>\d{1,2})/$',user_find),
    url(r'^user/check/(?P<userid>\d{1,2})/(?P<team_id>\d{1,2})/(?P<flag>\d{1,2})/$',check1),    
    url(r'^information/$',information),
    url(r'^information/change_inf/$',ch_information),
    url(r'^information/change_img/$',ch_img),
    url(r'^information/change_pass/$',ch_pass),
    url(r'^aim/$',aim),
    url(r'^aim/add/$',aim_add),
    url(r'^aim/change/$',aim_change),
    url(r'^aim/delete/$',aim_delete),
    url(r'^search/$',search),
    url(r'^diary/$',diary),
    url(r'^mydiary/$',mydiary),
    url(r'^diary/(?P<diaryid>\d{1,2})/$',diary_inf),
    url(r'^diary/add/$',dia_gui_add),
    url(r'^diary/delete/$',diary_delete),
    url(r'^diary/change/$',diary_change),
    url(r'^team/$',team),
    url(r'^team/new/(?P<aim_id>\d{1,2})/$',team_add),
    url(r'^team/del/(?P<team_id>\d{1,2})/$',team_del),
    url(r'^team/addMem/(?P<team_id>\d{1,2})/$',teamMemAdd),
    url(r'^team/add2/$',teamAdd),
    url(r'^team/find/$',teamfind),   
    url(r'^guide/$',guide),
    url(r'^guide/inf/$',guideInfor),
    url(r'^guide/add/$',guideAdd),
    url(r'^guide/zan/$',guide_zan),
    url(r'^guide/myguide/$',myguide),
    url(r'^guide/change/$',guide_change),
    url(r'^guide/delete/$',guide_delete),
    url(r'^forum/$',forum),
    url(r'^file/$',file),
    url(r'^check/(?P<team_id>\d{1,2})/(?P<flag>\d{1,2})/$',check),
    url(r'^diary/pinglun/$',pinglun1),
    url(r'^guide/pinglun/$',pinglun2),
    url(r'^admin/$',admin),
    url(r'^admin/login/$',admin_login),
    url(r'^admin/logout/$',admin_logout),
    url(r'^admin/finduser/$',admin_finduser),
    url(r'^admin/reset/$',admin_resetpass),
    url(r'^admin/guide/$',admin_guide),
    url(r'^admin/guidecheck/$',admin_guidecheck),
    
]