import re

html_text = """<div class="timeline"><div class="timeline-item" data-text="Band"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/4-qbtL4D3D.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Band"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/32-e8vF3_Uz.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Band"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/33-4DhItYUo.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="EDM Night"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/17-mywrk4HG.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Muscial Events"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/9-n7_g660t.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Solo Performances"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/27-2DxCzicw.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Mob Dance"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/23-InBsinfl.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Open Mic"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/10-QgmdnGch.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Quizes"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/30-8oKxTiDe.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Canon Event"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/28-Iy5hV6ZN.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Awards"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/16-ivRF_0vi.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="MUN"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/22-7w7FsVF8.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Mask It Up"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/31-zNFkWWqg.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Treasure Hunt"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/29-MuS_3YBU.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Traditional Dance"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/25-MY4hzVY6.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Rock Dance"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/26-WftiWDge.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="POP Dance"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/34-r6VaU32t.jpg" alt="image"></div></div></div><div class="timeline-item" data-text="Cultural Dance"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/13-CKJmHeCM.jpg" alt="image"></div></div></div><div class="timeline-item timeline-item--active" data-text="Social Camps"><div class="timeline__content"><div class="timeline_img_div"><img class="timeline__img" src="/assets/35-OiDsO2m6.jpg" alt="image"></div></div></div></div>"""

# Use regular expression to find all data-text values
data_text_values = re.findall(r'data-text="([^"]+)"', html_text)

print(data_text_values)