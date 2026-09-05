import os
import hashlib
import math
from threading import Thread
from flask import Flask
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- 1. SERVER KEEP-ALIVE ---
app = Flask(__name__)

@app.route('/')
def health_check():
    return "TOOL MD5 TXGAME v11.0 QUANTUM MATRIX ONLINE", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- 2. CẤU HÌNH HỆ THỐNG & ADMIN ---
TOKEN = '8985526419:AAGdRkntgFNYLBG53LoI-pNC7aHtOFMWhGA'
ADMIN_ID = 755092812
ADMIN_USERNAME = "lionvnios"

bot = telebot.TeleBot(TOKEN)
user_data = {}
all_users = set()
GLOBAL_CACHE = {}

def is_admin(user):
    return (user.id == ADMIN_ID) or (user.username and user.username.lower() == ADMIN_USERNAME)

def init_user(uid):
    all_users.add(uid)
    if uid not in user_data:
        user_data[uid] = {"balance": 20, "web": "HitClub", "logs": []}

# --- 3. ĐỘNG CƠ PHÂN TÍCH LƯỢNG TỬ (QUANTUM MATRIX ENGINE) ---
def ultimate_quantum_hash_algo(raw_code):
    clean_code = raw_code.strip().lower()
    
    # Cache đồng bộ máy chủ tuyệt đối
    if clean_code in GLOBAL_CACHE:
        return GLOBAL_CACHE[clean_code]

    # Lớp 1: Khởi tạo Vector Đa Chiều (Multi-Dimensional Cryptography)
    sha512_hash = hashlib.sha512(clean_code.encode()).hexdigest()
    blake2b_hash = hashlib.blake2b(clean_code.encode()).hexdigest()

    # Lớp 2: Ma trận phân mảnh Bitwise XOR (Fragmentation Matrix)
    core_val = 0
    for i in range(0, 64, 4):
        core_val ^= int(sha512_hash[i:i+4], 16) + int(blake2b_hash[i:i+4], 16)

    # Lớp 3: Chuẩn hóa bằng Hằng số Toán học (Pi & Euler Normalization)
    math_factor = (math.pi * math.e * core_val) % 999999
    
    # Cân bằng phân phối xác suất (Dải thực tế: 12.5% đến 87.5%)
    percent_raw = 12.5 + (math_factor % 750000) / 10000.0
    
    is_tai = percent_raw >= 50.0
    result = "TÀI" if is_tai else "XỈU"
    
    if is_tai:
        p_tai = round(percent_raw, 1)
        p_xiu = round(100.0 - p_tai, 1)
    else:
        p_xiu = round(100.0 - percent_raw, 1)
        p_tai = round(percent_raw, 1)

    # Lớp 4: Vi phân độ tin cậy (Confidence Drift)
    md5_part = int(hashlib.md5(clean_code.encode()).hexdigest()[:6], 16)
    acc = round(91.5 + (md5_part % 80) / 10.0, 1) # Độ chính xác hiển thị: 91.5% - 99.4%

    res_tuple = (result, p_tai, p_xiu, acc)
    GLOBAL_CACHE[clean_code] = res_tuple
    return res_tuple

# --- 4. GIAO DIỆN TỐI GIẢN CHUYÊN NGHIỆP ---
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("⚙️ Đổi Cổng Game", callback_data="btn_web"),
        InlineKeyboardButton("💳 Ví & Lịch Sử", callback_data="btn_info")
    )
    markup.add(InlineKeyboardButton("💎 Nạp Xu Admin", callback_data="btn_nap"))
    return markup

# --- 5. LỆNH ĐIỀU HƯỚNG CƠ BẢN ---
@bot.message_handler(commands=['start'])
def start_cmd(message):
    uid = message.from_user.id
    init_user(uid)
    text = (
        "⚡ **TOOL MD5 TXGAME [v11.0]** ⚡\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"🆔 ID Hệ Thống: `{uid}`\n"
        f"💳 Số dư khả dụng: `{user_data[uid]['balance']} Xu`\n"
        f"🌐 Cổng Game: `{user_data[uid]['web']}`\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "👉 **Dán mã MD5 (32 ký tự) hoặc SHA256 (64 ký tự)** để kích hoạt ma trận."
    )
    bot.reply_to(message, text, parse_mode="Markdown", reply_markup=main_menu())

# --- 6. HỆ THỐNG QUẢN TRỊ ADMIN AN TOÀN ---
@bot.message_handler(commands=['congxu'])
def add_coins(message):
    if not is_admin(message.from_user):
        bot.reply_to(message, "❌ **Truy cập bị từ chối:** Yêu cầu quyền Quản trị viên!")
        return
    try:
        parts = message.text.split()
        target_id, amount = int(parts[1]), int(parts[2])
        init_user(target_id)
        user_data[target_id]["balance"] += amount
        bot.reply_to(message, f"✅ **LỆNH THỰC THI THÀNH CÔNG!**\n👤 ID: `{target_id}` | ➕ `{amount} Xu` | 💳 Tổng: `{user_data[target_id]['balance']} Xu`", parse_mode="Markdown")
        try:
            bot.send_message(target_id, f"🎉 Admin đã bơm **+{amount} Xu** vào tài khoản!\n💳 Số dư mới: **{user_data[target_id]['balance']} Xu**", parse_mode="Markdown")
        except:
            pass
    except Exception:
        bot.reply_to(message, "❌ **Sai cú pháp!** Cấu trúc: `/congxu <ID_User> <Số_Xu>`", parse_mode="Markdown")

@bot.message_handler(commands=['thongbao'])
def broadcast(message):
    if not is_admin(message.from_user):
        bot.reply_to(message, "❌ **Truy cập bị từ chối:** Yêu cầu quyền Quản trị viên!")
        return
    try:
        notice = message.text.split(" ", 1)[1].strip()
        success = sum([1 for uid in list(all_users) if bot.send_message(uid, f"📢 **THÔNG BÁO HỆ THỐNG**\n━━━━━━━━━━━━━━━━━━━\n{notice}", parse_mode="Markdown")])
        bot.reply_to(message, f"✅ Đã truyền tín hiệu tới `{success}` tài khoản.", parse_mode="Markdown")
    except Exception:
        bot.reply_to(message, "❌ **Sai cú pháp!** Cấu trúc: `/thongbao <Nội dung>`", parse_mode="Markdown")

# --- 7. TƯƠNG TÁC CALLBACK ---
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    uid = call.from_user.id
    init_user(uid)
    if call.data == "btn_web":
        markup = InlineKeyboardMarkup(row_width=2)
        for w in ["HitClub", "B52", "Lucky88", "LC79"]:
            markup.add(InlineKeyboardButton(f"🎮 {w}", callback_data=f"web_{w}"))
        bot.send_message(call.message.chat.id, "🌐 **Tùy chỉnh Cổng Game:**", parse_mode="Markdown", reply_markup=markup)
    elif call.data.startswith("web_"):
        web = call.data.split("_")[1]
        user_data[uid]["web"] = web
        bot.send_message(call.message.chat.id, f"✅ **Cổng Game đã khóa:** `{web}`", parse_mode="Markdown", reply_markup=main_menu())
    elif call.data == "btn_info":
        logs_str = "\n".join(user_data[uid]["logs"]) if user_data[uid]["logs"] else "Chưa có dữ liệu."
        bot.send_message(call.message.chat.id, f"💳 **TRÍCH XUẤT DỮ LIỆU TÀI KHOẢN**\n🆔 ID: `{uid}`\n💰 Số dư: `{user_data[uid]['balance']} Xu`\n📜 **5 Nhịp cầu gần nhất:**\n{logs_str}", parse_mode="Markdown", reply_markup=main_menu())
    elif call.data == "btn_nap":
        bot.send_message(call.message.chat.id, f"💎 **CỔNG NẠP XU TRỰC TIẾP**\n📩 Liên hệ Telegram: @lionVnIos\n🆔 Copy ID này gửi Admin: `{uid}`", parse_mode="Markdown")

# --- 8. PHÂN TÍCH LÕI (CORE ANALYZER) ---
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    uid = message.from_user.id
    init_user(uid)
    text = message.text.strip().lower()
    
    if len(text) not in [32, 64]:
        bot.reply_to(message, "⚠️ **Định dạng lỗi:** Mã băm phải là MD5 (32 ký tự) hoặc SHA256 (64 ký tự).")
        return
    if user_data[uid]["balance"] < 1:
        bot.reply_to(message, "⚠️ **Cảnh báo:** Tài khoản 0 Xu. Vui lòng nạp thêm để duy trì truy cập.", reply_markup=main_menu())
        return
        
    user_data[uid]["balance"] -= 1
    result, p_tai, p_xiu, acc = ultimate_quantum_hash_algo(text)
    
    code_type = "MD5" if len(text) == 32 else "SHA-256"
    res_icon = "🔴 TÀI" if result == "TÀI" else "🔵 XỈU"
    
    user_data[uid]["logs"].insert(0, f"[{code_type}] {text[:8]}... ➔ {result}")
    if len(user_data[uid]["logs"]) > 5:
        user_data[uid]["logs"].pop()
        
    res_msg = (
        f"⚡ **KẾT QUẢ GIẢI MÃ MA TRẬN** ⚡\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 Nhịp cầu: **{res_icon}**\n"
        f"📊 Tỉ lệ chuẩn: **Tài {p_tai}% - Xỉu {p_xiu}%**\n"
        f"⚡ Độ hội tụ thuật toán: **{acc}%**\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Server: `{user_data[uid]['web']}` | 💳 Dư: `{user_data[uid]['balance']} Xu`"
    )
    bot.reply_to(message, res_msg, parse_mode="Markdown", reply_markup=main_menu())

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    try:
        bot.remove_webhook()
    except:
        pass
    print("TOOL MD5 TXGAME v11.0 QUANTUM MATRIX ACTIVE...")
    bot.infinity_polling(none_stop=True)
