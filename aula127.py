import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array, load_img


# Aumento aleatório de dados (Redimensionamento, Rotação, Inversões, Zoom, Deslocamentos) usando ImageDataGenerator 
training_data_generator = ImageDataGenerator(
    rescale = 1.0/255,
    rotation_range=40,
    width_shift_range=0.3,
    height_shift_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest')


# Diretório de Imagens
training_image_directory = "PRO_1-4_C127_PneumothoraxImageDataset/training_dataset"

# Gere arquivos de imagem aumentada
training_augmented_images = training_data_generator.flow_from_directory(
    training_image_directory,
    target_size=(180,180))

# Aumento aleatório de dados (redimensionamento) usando ImageDataGenerator
validation_data_generator = ImageDataGenerator(rescale = 1.0/255)

# Diretório de Imagens
validation_image_directory = "PRO_1-4_C127_PneumothoraxImageDataset/validation_dataset"

# Gere dados aumentados pré-processados
validation_augmented_images = validation_data_generator.flow_from_directory(
    validation_image_directory,
    target_size=(180,180))

training_augmented_images.class_indices

model = tf.keras.models.Sequential([
    
    # Primeira camada de Convolução e Pooling
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(180, 180, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),

    # Segunda camada de Convolução e Pooling
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Terceira camada de Convolução e Pooling
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Quarta camada de Convolução e Pooling
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Achatar (flatten) os resultados para alimentar em uma camada densa
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),

    # Camada de classificação
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(2, activation='sigmoid')
])
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(training_augmented_images, epochs=20, validation_data = validation_augmented_images, verbose=True)

model.save("Pneumothorax.h5")