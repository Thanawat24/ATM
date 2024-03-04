import streamlit as st

st.markdown(
    """
    <style>
        .reportview-container {
            background: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fa0%2Fa0%2F16%2Fa0a01608a0386ad052a15a5af8196be7.png&tbnid=mT-LEhDjgRGC3M&vet=12ahUKEwjlx5X-4MuEAxV8jWMGHdnfAVwQMygAegQIARBJ..i&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F727964727259372126%2F&docid=x4rP57aAVp7pcM&w=1920&h=1080&q=pixel%20art%201920x&ved=2ahUKEwjlx5X-4MuEAxV8jWMGHdnfAVwQMygAegQIARBJ")
        }
    </style>
    """,
    unsafe_allow_html=True
)

#รับรหัสผ่านจากผู้ใช้
password = st.text_input("กรุณาใส่รหัสผ่าน", type="password")

#รวจสอบว่ารหัสผ่านถูกต้องหรือไม่
if password == "152201":
        #st.success("รหัสผ่านถูกต้อง! คุณสามารถเข้าถึงฟีเจอร์หรือข้อมูลได้")

        account_balance = 10000 

#รับรหัสผ่านอีกครั้ง
        password_check = st.text_input("กด1 เพื่อดูเงิน กด2 เพื่อถอนเงิน", type="password")

#ตรวจสอบว่ารหัสผ่านอีกครั้งถูกต้องหรือไม่
        if password_check == "1":
            #st.success("รหัสผ่านถูกต้อง! คุณสามารถเข้าถึงฟีเจอร์หรือข้อมูลได้")
        # ตรวจสอบยอดเงินในบัญชี
            account_balance = 10000  # สมมติว่ามีเงินในบัญชี 10,000 บาท
            st.write(f"ยอดเงินในบัญชีของคุณ: {account_balance} บาท")
   
        elif password_check == "2":
        #st.success("รหัสผ่านถูกต้อง! คุณสามารถเข้าถึงฟีเจอร์หรือข้อมูลได้")
        #User input for withdrawal amount
            withdrawal_amount = st.number_input("Enter the amount you want to withdraw:", min_value=0, max_value=30000, step=100)

        #Validating the withdrawal amount
            while withdrawal_amount % 100 != 0:
                st.warning("Withdrawal amount must be in multiples of 100.")
                withdrawal_amount = st.number_input("Enter the amount you want to withdraw:", min_value=0, max_value=30000, step=100)

            if withdrawal_amount > account_balance:
                st.error("ขออภัย ยอดเงินในบัญชีของคุณไม่เพียงพอสำหรับการถอนเงินนี้")

            else:
        
        #Calculating the number of banknotes
                num_1000 = withdrawal_amount // 1000
                num_500 = (withdrawal_amount % 1000) // 500
                num_100 = (withdrawal_amount % 500) // 100

        #Displaying the number of banknotes
                st.write(f"Number of 1000 baht banknotes: {num_1000}")
                st.write(f"Number of 500 baht banknotes: {num_500}")
                st.write(f"Number of 100 baht banknotes: {num_100}")

                account_balance -= withdrawal_amount
                st.write(f"ยอดเงินคงเหลือ: {account_balance} บาท")
    
else:
        st.error("รหัสผ่านไม่ถูกต้อง! กรุณาลองใหม่")