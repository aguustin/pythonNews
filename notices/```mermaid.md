```mermaid

---
title: News
---

erDiagram:

Users{
    int usersId PK
    file profile
    string firstName
    string lastName
    string mail
    string password
    int type
}

News{
    int newsId PK
    string title
    string subtitle
    file imageTitle
    string firsParagraph
    string secondParagraph
    string thirdParagraph
    file firstImage
    file secondImage
    file thirdImage
}

Categories{
    int categoriesId PK
    string categories
}

Users_News{
    int Users FK
    int news FK
}

Categories_News{
    int categories FK
    int news FK
}