import streamlit as st

st.title("Congratulations!!")
st.header("""Em biết rằng không còn bao lâu nữa anh sẽ bước vào kì thi THPTQG đầy thách thức phía trước.
Hôm nay em làm web này để có thể gửi những lời chúc đầy ý nghĩa nhất""")

name = st.text_input("Nhập Họ và tên (Viết hoa toàn bộ) ")
code = st.text_input("Nhập code: ")

button = st.button("CHECK")

if button == True:
    if name == "NGUYỄN ANH DŨNG" and code == "08812A12":
        st.balloons()
        st.write("""Em chúc anh đậu tốt nghiệp và sẽ thực hiện được ước mơ của mình. Anh cũng chính là người thầy đã 
        chỉ dạy cho em về Arduino từ lúc em chưa biết gì đến khi em có thể tự ngồi code và fix lỗi. Nói thiệt anh giảng cho 
         em, em thấy rất là dễ hiểu và còn ngồi nói chính trị với em. Những thời gian ấy em rất trân trọng. Em chúc anh sẽ đạt 
         được ước mơ của mình nhe, và anh hãy luôn ở lại Tan Binh RBT để có thể dẫn dắt em tới nhiều chân trời mới trong lĩnh
         vực học thuât này ( Đừng có dựa vào quy tắc IELTS writing rồi đánh giá bình luận nha =))))) ) """ )

    elif name == "NINH THẾ ANH" and code == "09912A5":
        st.balloons()
        st.write("""Em chúc anh đậu tốt nghiệp và sẽ thực hiện được ước mơ của mình. Nhờ bài thi NCKH của anh mà em được học hỏi,
        mở mang tầm mắt. Anh cũng đã cho em thêm động lực và sức mạnh để mạnh dạn học NCKH. Cuối cùng, Em chúc anh sẽ đạt
        được ước mơ của mình nhe, và anh hãy luôn ở lại Tan Binh RBT để có thể dẫn dắt em tới nhiều chân trời mới trong lĩnh
        vực học thuât này""")

    elif name == "TRẦN HOÀNG VIỆT" and code == "01812A13":
        st.balloons()
        st.write("""Em chúc anh đậu tốt nghiệp và sẽ thực hiện được ước mơ của mình. Nhờ bài thi NCKH của anh mà em được học hỏi
        mở mang tầm mắt, đặc biệt là cái AI. Em rất thích AI và muốn phát triển nó trong tương lai. Web mà anh đang đọc này cũng
        chính tay em viết và não em suy nghĩ từng dòng code mà được học qua khóa học AI. Mà giờ anh sắp bước vào kỳ thi THPTQG thì 
        em chúc anh sẽ đạt được ước mơ của mình nhe, và anh hãy luôn ở lại Tan Binh RBT để có thể dẫn dắt em tới nhiều chân trời mới trong lĩnh
        vực học thuât này""")

    elif name == "NGUYỄN HOÀNG THÀNH LONG" and code == "02712A4":
        st.balloons()
        st.write("""Em chúc anh đậu tốt nghiệp và sẽ thực hiện được ước mơ của mình. Rồi sẽ trở thành pilot nhaa =)))))) """)

    elif name == "Vũ Nam" and code == "03812A12":
        st.balloons()
        st.write("""Em chúc anh đậu tốt nghiệp và sẽ thực hiện được ước mơ của mình, và mong anh hãy luôn ở lại Tan Binh RBT để có thể dẫn dắt em tới nhiều chân trời mới trong lĩnh
        vực học thuât này """)
    else:
        st.write("VUI LÒNG NHẬP TÊN VÀ CODE LẠI")