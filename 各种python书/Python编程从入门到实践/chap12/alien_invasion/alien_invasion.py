# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/13 7:37
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
<<<<<<< HEAD
=======
from time import sleep
from game_stats import GameStats
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 设置背景颜色
        self.bg_color = (230, 230, 230)
<<<<<<< HEAD
=======
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """创建外星人群"""
<<<<<<< HEAD
        #创建一个外星人并计算一行可容纳多少个外星人
        #外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x //(2*alien_width)
        #创建第一行外星人。
        for alien_number in range(number_aliens_x):
            #创建一个外星人并将其加入当前行。
            alien = Alien(self)
            alien.x = alien_width +2 *alien_width *alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)
        self.aliens.add(alien)

=======
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # 创建外形人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):

        # 创建第一行外星人,并将其放在第一行。
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取响应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
    def _check_events(self):
        """响应按键和鼠标事件"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
<<<<<<< HEAD
        #更新子弹的位置
=======
        # 更新子弹的位置
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
<<<<<<< HEAD
            # print(len(self.bullets))

=======

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞。"""
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # 删除现有的子弹并创建一群外星人。
            self.bullets.empty()
            self._create_fleet()
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
<<<<<<< HEAD
            self.ship.update()
            self._update_bullets()
=======
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
            self._update_screen()

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

<<<<<<< HEAD
    def _check_keydown_events(self,event):
=======
    def _check_keydown_events(self, event):
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

<<<<<<< HEAD
    def _check_keyup_events(self,event):
=======
    def _check_keyup_events(self, event):
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """"创建一颗子弹，并将其加入编组bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
<<<<<<< HEAD

            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)

=======
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置。"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将ships_left 减1
            self.stats.ships_left -= 1

            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break

>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
