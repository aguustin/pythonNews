import axios from 'axios';

export const uploadNewRequest = (formData) => axios.post('http://127.0.0.1:8000/uploadNew/',formData)


/*    path('createCategory/', csrf_exempt(views_notices.Create_category.as_view()), name="create_category"),
    path('createNew/', csrf_exempt(views_notices.Create_New.as_view()), name="create_new"),
    path('getAllNews/', views_notices.Get_All_News_Categories.as_view(), name="get_all_new_and_categories"),
    path('getNewByCategory/<int:categoryId>/', views_notices.Get_New_by_Category_Id.as_view(), name="get_news_by_category"),
    path('getNew/<int:newId>/', views_notices.Get_New_Id.as_view(), name="get_new"),
    path('updateNew/', csrf_exempt(views_notices.Update_New.as_view()), name="update_new") */