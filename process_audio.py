
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import librosa as lb
from librosa.display import specshow

# Sound
import soundfile as snd

# Time
import time as tm

from util import get_dir, get_nome_info


dir = []
labels = []
signals = []
resampling = []
rates = []
sizes = []
durations = []
spectrograms = []
wlengths = []
hlengths = []
dir_images = []


diretorio_base = '/home/falanga/Downloads/jordana-py/saida/control/water/'

soundPaths = get_dir(diretorio_base, 0)

for soundPathName in soundPaths:

    try:
        soundPath = diretorio_base + soundPathName
        label = soundPath.split(os.path.sep)[-2]
        #Verifica informaçoes do arquivo wave
        audio_signal, sampling_rate = snd.read(soundPath)

        # Resampling
        resampling.append(lb.resample(audio_signal, sampling_rate, 8000))

        # update the data lists, respectively
        dir.append(soundPath)
        dir_images.append("Imagens/" + label + "/" + (soundPath.split(os.path.sep)[-1]).replace('.wav', '.png'))
        labels.append(label)
        rates.append(sampling_rate)
        signals.append(audio_signal)
        sizes.append(audio_signal.shape[0])
        durations.append(audio_signal.shape[0] / sampling_rate)

        # Spectogram
        window_length = int(0.025 * sampling_rate)
        wlengths.append(window_length)

        hop_length = int(0.01 * sampling_rate)
        hlengths.append(hop_length)

        spectrograms.append(np.abs(lb.stft(audio_signal, hop_length=hop_length, win_length=window_length)))

    except ValueError:
        print("nada")


    df = pd.DataFrame({'dir': dir,
                       'dir_images': dir_images,
                       'labels': labels,
                       'rates': rates,
                       'sizes': sizes,
                       'durations': durations,
                       'signals': signals,
                       'resampling': resampling,
                       'spectrograms': spectrograms,
                       'windows_lengths': wlengths,
                       'hop_lengths': hlengths})

    print("✅ Arquivando dataframe.")
    try:
        # print("OK")
        df = df.sort_values(['dir_images'])
        # df.to_excel("/content/drive/MyDrive/Projeto_Fala/data.xlsx", index = False)
        df.to_excel("/home/falanga/workspaces/conda/jordana/data.xlsx", index=False)
    except OSError as e:
        print(f"Não foi salvar dataframe:{e.strerror}")

    end = tm.time()



start = tm.time()
print("⚙️ Iniciando exportação de espectrogramas.")

for i in range(len(df)):
    specshow(lb.amplitude_to_db(df.loc[i, "spectrograms"], ref=np.max),
             sr=df.loc[i, "rates"], hop_length=df.loc[i, "hop_lengths"],
             y_axis='linear', x_axis='time')
    # --plt.title('Spectrogram')
    # --plt.colorbar(format='%+2.0f dB')
    plt.axis('off')
    plt.tight_layout()
    # --plt.savefig("Imagens/"+label+'/'+(df.loc[i,"dir"].split(os.path.sep)[-1]).replace('.wav','.png'), format='png')
    # --plt.savefig("/content/drive/MyDrive/Projeto_Fala/Imagens/"+label+'/'+(df.loc[i,"dir"].split(os.path.sep)[-1]).replace('.wav','.png'), format='png')

    # plt.savefig("/content/drive/MyDrive/Projeto_Fala/"+df.loc[i,"dir_images"])
    x = df.loc[i, "dir_images"].rfind("/")

    diretorio = df.loc[i, "dir_images"][0:x]
    print ("DIR", diretorio)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    plt.savefig("/home/falanga/workspaces/conda/jordana/" + df.loc[i, "dir_images"])

print("✅ Arquivando dataframe.")

end = tm.time()
print("✅ Concluído exportação de espectrogramas. Execução: {} segundos.".format(round(end - start, 2)))
