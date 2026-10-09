import tensorflow as tf
from tensorflow.keras import layers, models
# Đọc bộ dữ liệu chữ số MNIST qua Keras.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# Đưa ảnh về tensor (batch, 28, 28, 1) và chuẩn hóa pixel về [0, 1].
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
# CNN (Convolutional Neural Network): mạng nơ-ron tích chập phân loại 10 chữ số.
model = models.Sequential([
    layers.Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])
# Cấu hình mô hình
model.compile(
    optimizer="adam", # Adam là thuật toán cập nhật trọng số dựa trên gradient, có learning rate thích nghi cho từng tham số.
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
# Huấn luyện 5 epoch (lượt đi qua toàn bộ dữ liệu huấn luyện).
# Hiện dùng tập test làm validation; cần tách riêng trước khi báo cáo kết quả test.
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
# Ghi đè model HDF5 trong thư mục làm việc hiện tại.
model.save("digit_model.h5")

print("Đã lưu model: digit_model.h5")
